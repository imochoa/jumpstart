#!/usr/bin/env python3
# stdlib imports
import pathlib
from pathlib import Path
import typing as T

# 3rd party imports
import click
from loguru import logger
import rich.color
from rich.filesize import decimal
from rich.markup import escape
from rich.text import Text
from rich.tree import Tree
import typer

# 1st party imports
from jumpstart.constants import FILES, PATHS
from jumpstart.core import loop_over_pkg_jsons, loop_over_pkgs, validate_schemas
from jumpstart.schemas import PackageMetadata, dump_json, load_json
from jumpstart.templates import PARAMS_TYPE, cog_param, get_param_schema
from jumpstart.templates.bin import BinParams
from jumpstart.templates.deb import DebParams
from jumpstart.templates.manual import NoParams
from jumpstart.templates.pipx import PipxParams

app = typer.Typer()

# typer & rich-cli
# https://pybash.medium.com/interactive-cli-1-40bc1df37df9


# @app.command()
# def create(item: str):
#     print(f"Creating item: {item}")


# @app.command()
# def delete(item: str):
#     print(f"Deleting item: {item}")


# @app.command()
# def sell(item: str):
#     print(f"Selling item: {item}")


# if __name__ == "__main__":
#     app()


def autogenerate(
    root: pathlib.Path = PATHS.PACKAGES_DIR,
    param_types: tuple[type, ...] = tuple(),
) -> None:
    """
    Loop over the default packages and:
    1. Check JSON files & set defaults
    2. Generate the templated files

    TODO define common filtering
    apply common filtering
    """

    # Test schemas in *root*
    validate_schemas(root, reexport=True)

    pkg_generator = loop_over_pkgs(root)
    if param_types:
        # Todo skip pkgs without params before real work?
        pkgs2skip: list[str] = []
        logger.info(f"Skipping:" + "\n\t> ".join(pkgs2skip))

    # Autogenerate templates in *root*
    for metadata, params in pkg_generator:
        logger.info(f"{metadata}\t[{metadata.json_path.relative_to(root)}]")
        for param in params:
            logger.info(f"\t{param.header}\t[{param.header.json_path.relative_to(root)}]")
            if param_types and not isinstance(param, param_types):
                logger.debug(f"\t\t> Skipping!")
                continue
            cog_param(param=param, metadata=metadata)


def pkg_tree() -> None:
    """
    Show a tree of all possible options
    apply common filtering?
    save as a JSON for HTML generation?
    """
    pass


def lookup() -> None:
    """
    Choose:
     1. a method (install, remove update)
     1. a list of packages
     2. resolve/check dependencies, get order
     3. show full command to run
     4. let the user choose if they should run it

    """
    pass


# TODO list tags
# TODO tree of packages with options


def run_cli() -> None:
    print("RUN!")
    app()


if __name__ == "__main__":
    param_types: tuple[type, ...]
    # All types
    param_types = tuple()
    # Filter only bin
    # param_types=(BinParams,)
    autogenerate(
        param_types=param_types,
    )
