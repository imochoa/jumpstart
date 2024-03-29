#!/usr/bin/env python3

# stdlib imports
import codecs
import inspect
import json
from pathlib import Path
import shutil
import subprocess
import typing as T

# 3rd party imports
from loguru import logger

# 1st party imports
from jumpstart.cogging import cog_subprocess
from jumpstart.constants import FILES, PATHS, SCRIPTS
from jumpstart.schemas.metadata import PackageMetadata

# local imports
from .apt import AptParams
from .bin import BinParams
from .cargo import CargoParams
from .deb import DebParams
from .flatpak import FlatpakParams
from .manual import NoParams
from .npx import NpxParams
from .pipx import PipxParams

PARAMS_TYPE = T.Union[AptParams | FlatpakParams | PipxParams | NpxParams | BinParams, DebParams, NoParams | CargoParams]
PARAM_SCHEMA_MAP: T.Final[dict[str, T.Any]] = {
    sch.__module__.split(".")[-1]: sch
    for sch in (
        AptParams,
        DebParams,
        FlatpakParams,
        PipxParams,
        NpxParams,
        BinParams,
        NoParams,
    )
}


def get_param_schema(p: Path) -> PARAMS_TYPE:
    """
    Given a param JSON file, read the header.template key to find what schema should be used
    """
    with codecs.open(
        str(p.absolute()),
        "r",
        encoding="utf-8",
        errors="ignore",
    ) as fp:
        obj = json.load(fp)
    schema_key = obj["header"]["template"]
    schema = PARAM_SCHEMA_MAP[schema_key]
    return schema


COGMAIN_HEADER = "\n".join(
    (
        r'cog.outl(f"#!/bin/bash")',
        r'cog.outl(f"set -euo pipefail")',
        r'cog.outl(f"IFS=$\'\\n\\t\'")',
        r'cog.outl(f"")',
        r'cog.outl(f"# <<<AUTOGENERATED - DO NOT MODIFY>>>")',
        r'cog.outl(f"#\t\t >     File: {FILE}")',
        r'cog.outl(f"#\t\t >     Name: {NAME}")',
        r'cog.outl(f"#\t\t > Template: {TEMPLATE}")',
        r'cog.outl(f"")',
    )
)
COGPRE_HEADER = "\n".join(
    (
        r'cog.outl(f"# <<<PRE STAGE>>>")',
        r'cog.outl(f"")',
    )
)
COGPOST_HEADER = "\n".join(
    (
        r'cog.outl(f"# <<<POST STAGE>>>")',
        r'cog.outl(f"")',
    )
)


def cog_param(
    param: PARAMS_TYPE,
    metadata: PackageMetadata | None = None,
) -> None:
    """
    Run cog:
    1. Replace dst with src templates
    2. Use data/subfolder (post_install ...)
    """
    if isinstance(param, NoParams):
        logger.info(f"Skipping manual script: {NoParams}")
        return None

    default_cog_kwargs: dict[str, str] = dict(
        TEMPLATE=param.header.template,
        NAME="" if metadata is None else metadata.name,
    )

    dst_dir = param.header.json_path.parent

    template_root = Path(inspect.getfile(type(param))).parent
    templates = [f for f in template_root.iterdir() if f.stem in SCRIPTS.as_set()]
    template_map = {t: dst_dir / t.name for t in templates}
    include_paths = [template_root, PATHS.REPO_DIR]

    for src, dst in template_map.items():
        cog_args = {
            **param.cog_args,
            **default_cog_kwargs,
            **dict(FILE=src.name),
            **param.header.default_env.cog_args,
        }
        p = cog_subprocess(
            in_path=src,
            out_path=dst,
            include_paths=include_paths,
            cog_args=cog_args,
            prologue=COGMAIN_HEADER,
        )
        if p.returncode != 0:
            raise OSError(f"Error running {dst}:\n{p.stderr.decode('utf-8')}")
        logger.debug(f"\t\tcog {dst}")

    # Pre/Post templates
    pre_dir = dst_dir / FILES.PRE_DIR
    if pre_dir.is_dir():
        pre_templates = [f for f in pre_dir.iterdir() if f.stem in SCRIPTS.as_set()]
        pre_template_map = {t: dst_dir / t.name for t in pre_templates}
        for src, dst in pre_template_map.items():
            pre_cog_args = {
                **param.cog_args,
                **default_cog_kwargs,
                **dict(FILE=src.name.upper()),
            }
            pre_p = cog_subprocess(
                in_path=src,
                out_path=None,  # Write to stdout!
                include_paths=include_paths,
                cog_args=pre_cog_args,
                prologue=COGPRE_HEADER,
            )
            if pre_p.returncode != 0:
                raise OSError(f"Error running {dst}:\n{pre_p.stderr.decode('utf-8')}")

            # TODO write after all lines that start with comments & before content
            with open(dst) as fp:
                txt = fp.readlines()
            pre_start_idx = next(
                idx for idx, line in enumerate(txt) if line.strip() and not line.strip().startswith("#")
            )
            pre_txt = [line + "\n" for line in pre_p.stdout.decode("utf-8").split("\n")]
            txt = txt[:pre_start_idx] + pre_txt + txt[pre_start_idx:]
            with open(dst, "w") as fp:
                fp.write("".join(txt))

    post_dir = dst_dir / FILES.POST_DIR
    if post_dir.is_dir():
        post_templates = [f for f in post_dir.iterdir() if f.stem in SCRIPTS.as_set()]
        post_template_map = {t: dst_dir / t.name for t in post_templates}
        for src, dst in post_template_map.items():
            post_cog_args = {
                **param.cog_args,
                **default_cog_kwargs,
                **dict(FILE=src.name.upper()),
            }
            post_p = cog_subprocess(
                in_path=src,
                out_path=None,  # Write to stdout!
                include_paths=include_paths,
                cog_args=post_cog_args,
                prologue=COGPOST_HEADER,
            )
            if post_p.returncode != 0:
                raise OSError(f"Error running {dst}:\n{post_p.stderr.decode('utf-8')}")
            with open(dst, "a") as fp:
                fp.write("\n" + post_p.stdout.decode("utf-8"))

    return None
