#!/usr/bin/env python3

# stdlib imports
from pathlib import Path
import subprocess

# 3rd party imports
from loguru import logger


def cog_subprocess(
    in_path: Path,
    out_path: Path | None = None,
    include_paths: list[Path] | None = None,
    cog_args: dict[str, str] | None = None,
    prologue: str = "",
) -> subprocess.CompletedProcess[bytes]:
    """

    if *out_path* is None, use STDOUT


    -c          Checksum the output to protect it against accidental change.

    -d          Delete the generator code from the output file.

    -e          Warn if a file has no cog code in it.

    -U          Write the output with Unix newlines (only LF line-endings).

    --verbosity=VERBOSITY
                Control the amount of output. 2 (the default) lists all files,
                1 lists only changed files, 0 lists no files.
    """
    basic_cog = ["cog", "-e", "-U", "-d", "-c"]

    if prologue:
        basic_cog += ["-p", prologue]

    include_cmd: list[str] = []
    if include_paths:
        include_cmd = sum((["-I", str(p)] for p in include_paths), [])
    args_cmd: list[str] = []
    if cog_args:
        args_cmd = sum([["-D", f"{k.upper()}={v}"] for k, v in cog_args.items()], [])

    out_cmd: list[str] = []
    if out_path is not None:
        out_cmd = ["-o", str(out_path)]

    cog_cmd = basic_cog + args_cmd + include_cmd + out_cmd + [str(in_path)]
    logger.debug(f"Running: {' '.join(cog_cmd)}")
    return subprocess.run(cog_cmd, capture_output=True)
