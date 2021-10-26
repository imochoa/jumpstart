#!/usr/bin/env python3

# stdlib imports
import logging
import os

# import enum
import pathlib
import re
import stat
import typing as T

# 1st party imports
from jumpstart import Installable
from jumpstart.constants import INDEX_DIR, Architecture, OperatingSystem, System

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def instantiate_index_dir(
    filter_arch: str = "",
    filter_os: str = "",
) -> T.Iterable[Installable]:
    index_dir = INDEX_DIR

    SEP = "__"
    for top_dir in (d for d in index_dir.iterdir() if d.is_dir()):
        dir_arch, dir_os = Architecture.unknown, OperatingSystem.unknown
        if SEP in top_dir.name:
            pos = top_dir.name.find(SEP)
            dir_arch = Architecture(top_dir.name[:pos])
            dir_os = OperatingSystem(top_dir.name[pos + len(SEP) :])
        for installable_dir in (d for d in top_dir.iterdir() if d.is_dir()):
            try:
                yield Installable.from_dir(
                    installable_dir,
                    architecture=dir_arch,
                    operating_system=dir_os,
                )
            except Exception:
                logger.exception(f"Failed to instantiate: {installable_dir}")


def report() -> None:
    for obj in instantiate_index_dir():
        print(obj.architecture, obj)


# def refresh() -> None:
#     """
#     Checks the json files
#     warns about unknown names
#     regenerates the status scripts
#     """
#     for obj in instantiate_index_dir():
#         for alt in obj.alternatives:
#             alt.refresh()


def generate_std_scripts() -> None:
    for obj in instantiate_index_dir():
        print(obj.path.name)
        for alt in obj.alternatives:
            try:
                alt.generate_std_files()
            except Exception:
                logger.exception(f"FAILED [{obj}]: {alt}")


if __name__ == "__main__":
    report()
    generate_std_scripts()
