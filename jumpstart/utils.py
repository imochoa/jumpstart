#!/usr/bin/env python3

# stdlib imports
import codecs
import pathlib
import typing as T

#
# def get_runtime_arch() -> Architecture:
#     arch = Architectures.unknown
#     if platform.machine().endswith("64"):
#         arch = Architectures.x64
#     return arch
#
#
# def get_runtime_platform() -> Platform:
#     return Platform(platform.system())
#
#
# def get_runtime_os() -> OS:
#     os = OSs.unknown
#     if get_runtime_platform() == Platforms.linux:
#         p_stdout = subprocess.check_output(["lsb_release", "-a"])
#         if p_stdout:
#             os = OS(p_stdout.decode("utf8").split("\n")[1].split(":")[1].strip())
#     return os


# def similarity(a: str, b: str) -> float:
#     """
#     Compares 2 strings and returns a similarity between 0-1
#     """
#     return SequenceMatcher(None, a.lower(), b.lower()).ratio()
#


def safe_open(p: pathlib.Path, mode: T.Union[T.Literal["r", "w"]] = "r") -> codecs.StreamReaderWriter:
    return codecs.open(str(p), mode=mode, encoding="utf-8", errors="ignore")


# def load_script(p: pathlib.Path) -> T.List[str]:
#     """
#
#     Removes trailing and leading whitespace and escaped line breaks
#     ```
#     echo "hello" \
#     && echo "new line!"
#     ```
#     """
#     with safe_open(p) as fp:
#         lines = fp.readlines()
#
#     txt = "\n".join(line.strip() for line in lines)
#     return txt.replace("\\\n", " ").split("\n")

#
# def filewrite_log(p: pathlib.Path, logger:T.Any = logger) -> None:
#     logger.info(f"Wrote {p} {p.stat().st_size / 1e3:.2f} [Kb]")
