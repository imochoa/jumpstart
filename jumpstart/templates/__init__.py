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

PARAM_SCHEMA_MAP: T.Final[dict[str, T.Any]] = {sch.__module__.split(".")[-1]: sch for sch in (AptParams,)}


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


def cog_params(dir: pathlib.Path, params: AptParams) -> None:
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


# cog - generate content with inlined Python code.
#
# cog [OPTIONS] [INFILE | @FILELIST] ...
#
# INFILE is the name of an input file, '-' will read from stdin.
# FILELIST is the name of a text file containing file names or
#     other @FILELISTs.
#
# OPTIONS:
#     -c          Checksum the output to protect it against accidental change.
#     -d          Delete the generator code from the output file.
#     -D name=val Define a global string available to your generator code.
#     -e          Warn if a file has no cog code in it.
#     -I PATH     Add PATH to the list of directories for data files and modules.
#     -n ENCODING Use ENCODING when reading and writing files.
#     -o OUTNAME  Write the output to OUTNAME.
#     -p PROLOGUE Prepend the generator source with PROLOGUE. Useful to insert an
#                 import line. Example: -p "import math"
#     -P          Use print() instead of cog.outl() for code output.
#     -r          Replace the input file with the output.
#     -s STRING   Suffix all generated output lines with STRING.
#     -U          Write the output with Unix newlines (only LF line-endings).
#     -w CMD      Use CMD if the output file needs to be made writable.
#                     A %s in the CMD will be filled with the filename.
#     -x          Excise all the generated output without running the generators.
#     -z          The end-output marker can be omitted, and is assumed at eof.
#     -v          Print the version of cog and exit.
#     --check     Check that the files would not change if run again.
#     --markers='START END END-OUTPUT'
#                 The patterns surrounding cog inline instructions. Should
#                 include three values separated by spaces, the start, end,
#                 and end-output markers. Defaults to '[[[cog ]]] [[[end]]]'.
#     --verbosity=VERBOSITY
#                 Control the amount of output. 2 (the default) lists all files,
#                 1 lists only changed files, 0 lists no files.
#     -h          Print this help.
