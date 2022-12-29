#!/usr/bin/env python3

# stdlib imports
import codecs
import inspect
import json
import pathlib
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


def load_params(p: pathlib.Path) -> T.Any:
    with codecs.open(
        str(p.absolute()),
        "r",
        encoding="utf-8",
        errors="ignore",
    ) as fp:
        obj = json.load(fp)
    schema_key = obj["header"]["template"]
    schema = PARAM_SCHEMA_MAP[schema_key]
    return schema.Schema().load(obj)


def cog_params(dir: pathlib.Path, params: PARAMS_TYPE) -> None:
    """
    Run cog

    """
    template_root = pathlib.Path(inspect.getfile(type(params))).parent
    templates = [f for f in template_root.iterdir() if f.stem in SCRIPTS.as_set()]
    template_map = {t: dir / t.name for t in templates}

    basic_cog = ["cog", "-e", "-U", "-d", "-c"]
    include_paths = ["-I", str(PATHS.TEMPLATES_DIR)]

    for src, dst in template_map.items():
        cog_cmd = basic_cog + params.cog_args + include_paths + ["-o", str(dst)] + [str(src)]
        p = subprocess.run(cog_cmd, capture_output=True)
        if p.returncode != 0:
            raise OSError(f"Error running {dst}:\n{p.stderr.decode('utf-8')}")
        logger.debug(f"\t\tcog {dst}")

    return None
