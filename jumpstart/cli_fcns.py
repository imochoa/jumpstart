#!/usr/bin/env python3

# stdlib imports
import argparse
import concurrent.futures
import copy
import enum
from io import StringIO
import json
import logging
import os
import pathlib
import re
import stat
import sys
import typing as T

# 1st party imports
from jumpstart import Installable, Metadata
from jumpstart.cli_utils import bcolors, colorize, debug, error, info, warning
from jumpstart.constants import INDEX_DIR, Architecture, OperatingSystem, System
from jumpstart.utils import safe_open

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


def status_tree(installables: T.List[Installable]) -> str:
    report_str = "x64__ubuntu2004"
    inst_count = len(installables)
    for i_idx, inst in enumerate(installables):

        i_b1 = {inst_count - 1: "└──"}.get(i_idx, "├──")
        i_b2 = {"├──": "│"}.get(i_b1, " ")
        # buffer.write(f'\n├── {inst.path.name}')
        report_str += f"\n{i_b1} {inst.path.name}"

        if not inst.alternatives:
            # buffer.write('\n│')
            report_str += "\n│"
            continue

        for a_idx, alt in enumerate(inst.alternatives):
            a_b1 = {len(inst.alternatives) - 1: "└──"}.get(a_idx, "├──")
            symbol = {
                True: colorize(msg="v", color=bcolors.GREEN),
                False: colorize(msg="X", color=bcolors.FAIL),
                None: colorize(msg="?", color=bcolors.WARNING),
            }[alt.is_installed()]
            report_str += f"\n{i_b2}    {a_b1}  [{alt.dirname}] -> {symbol}"
    return report_str


def report() -> None:
    installables = list(instantiate_index_dir())

    def _cache_is_installed(inst: Installable) -> None:
        for alt in inst.alternatives:
            alt.is_installed()

    logger.info("Checking all statuses... (might take a bit)")
    with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
        executor.map(_cache_is_installed, installables)
    logger.info("Generating the tree...")
    # TODO CSVs...
    # buffer= StringIO()
    logger.setLevel(logging.ERROR)
    logging.disable()

    print(status_tree(installables))


def fill_default_metadata() -> None:

    for inst in instantiate_index_dir():
        if inst.metadata_json.is_file():
            m = Metadata.from_json(inst.metadata_json)
        else:
            m = Metadata()

        m.fill_with_defaults(inst.path)

        m.to_json(inst.metadata_json)


def generate_std_scripts() -> None:
    for obj in instantiate_index_dir():
        print(obj.path.name)
        for alt in obj.alternatives:
            try:
                alt.generate_std_files()
            except Exception:
                logger.exception(f"FAILED [{obj}]: {alt}")


def j_install(pkgs: T.List[str]) -> None:
    if not pkgs:
        print("list all pkgs")
        return
    print(f"Combine {pkgs} into a script")


def j_status(pkgs: T.List[str]) -> None:
    if not pkgs:
        print("list all pkgs")
        return
    print(f"Combine {pkgs} into a script")


def jumpstart() -> None:
    class Cmds(enum.Enum):
        install = "install"
        status = "status"
        dev = "dev"
        template = "template"
        regenerate = "regenerate"

    # create the top-level parser
    parser = argparse.ArgumentParser(prog="Jumpstart", description="Install things easily")
    parser.add_argument("--debug", action="store_true", help="debug mode")
    subparsers = parser.add_subparsers(help="sub-command help", dest="command")

    # create the parser for the "command_a" command
    parser_a = subparsers.add_parser(Cmds.install.value, help="Install anything help")
    parser_a.add_argument(
        "pkg(s)",
        type=str,
        nargs="*",
        help=('Installs the listed pkgs or prints out a list of the available pkgs, "' '"if none were specified'),
    )

    # create the parser for the "command_b" command
    parser_b = subparsers.add_parser(Cmds.status.value, help="command_b help")
    parser_b.add_argument("--baz", choices="XYZ", help="baz help")

    # create the parser for the "command_c" command
    parser_c = subparsers.add_parser(Cmds.template.value, help="template help")
    parser_c.add_argument("--baz", choices="XYZ", help="baz help")

    # create the parser for the "command_c" command
    parser_d = subparsers.add_parser(Cmds.regenerate.value, help="template help")
    parser_d.add_argument("--baz", choices="XYZ", help="baz help")

    args = parser.parse_args()

    if not args.command:
        error("\n\t- ".join(["You have to choose one of:"] + sorted(v.value for v in Cmds)))
        exit(1)

    cmd = Cmds(args.command)

    if cmd == Cmds.install:
        error("TODO")
    elif cmd == Cmds.status:
        info("Checking the status...")
        report()
    elif cmd == Cmds.regenerate:
        info("Regenerating auto files...")
        generate_std_scripts()
    else:
        pass
    info("Done!")


if __name__ == "__main__":
    report()
    # fill_default_metadata()
