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
from jumpstart.constants import PATHS, SCRIPTS

# local imports
from .apt import AptParams
from .bin import BinParams
from .flatpak import FlatpakParams
from .pipx import PipxParams

PARAMS_TYPE = T.Union[AptParams | FlatpakParams | PipxParams | BinParams]
PARAM_SCHEMA_MAP: T.Final[dict[str, T.Any]] = {
    sch.__module__.split(".")[-1]: sch
    for sch in (
        AptParams,
        FlatpakParams,
        PipxParams,
        BinParams,
    )
}


def get_param_schema(p: Path) -> PARAMS_TYPE:
    """
    Given a param JSON file, read the header.template key to find what schema schould be used
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


def cog_subprocess(
    in_path: Path,
    out_path: Path,
    include_paths: list[Path] | None,
    cog_args: dict[str, str] | None = None,
) -> subprocess.CompletedProcess[bytes]:
    """
    -c          Checksum the output to protect it against accidental change.

    -d          Delete the generator code from the output file.

    -e          Warn if a file has no cog code in it.

    -P          Use print() instead of cog.outl() for code output.

    -U          Write the output with Unix newlines (only LF line-endings).

    --verbosity=VERBOSITY
                Control the amount of output. 2 (the default) lists all files,
                1 lists only changed files, 0 lists no files.
    """
    basic_cog = ["cog", "-e", "-U", "-d", "-c"]
    include_cmd: list[str] = []
    if include_paths:
        include_cmd = sum((["-I", str(p)] for p in include_paths), [])
    args_cmd: list[str] = []
    if cog_args:
        args_cmd = sum([["-D", f"{k.upper()}={v}"] for k, v in cog_args.items()], [])

    cog_cmd = basic_cog + args_cmd + include_cmd + ["-o", str(out_path)] + [str(in_path)]
    logger.debug(f"Running: {' '.join(cog_cmd)}")
    return subprocess.run(cog_cmd, capture_output=True)


def cog_param(param: PARAMS_TYPE) -> None:
    """
    Run cog:
    1. Replace dst with src templates
    2. Use data/ subfolder (post_install ...)
    """
    dst_dir = param.header.json_path.parent

    template_root = Path(inspect.getfile(type(param))).parent
    templates = [f for f in template_root.iterdir() if f.stem in SCRIPTS.as_set()]
    template_map = {t: dst_dir / t.name for t in templates}

    for src, dst in template_map.items():
        p = cog_subprocess(
            in_path=src,
            out_path=dst,
            include_paths=[PATHS.TEMPLATES_DIR],
            cog_args=param.cog_args,
        )
        if p.returncode != 0:
            raise OSError(f"Error running {dst}:\n{p.stderr.decode('utf-8')}")
        logger.debug(f"\t\tcog {dst}")

    return None
