#!/usr/bin/env python3

# stdlib imports
import pathlib
import typing as T

# 3rd party imports
from loguru import logger
import rich.color
from rich.filesize import decimal
from rich.markup import escape
from rich.text import Text
from rich.tree import Tree
import typer

# 1st party imports
from jumpstart.constants import FILES, PATHS
from jumpstart.schemas import PackageMetadata, load_json

# def find_metadata_files(root:pathlib.Path=Paths.INDEX_DIR) -> T.Generator[PackageMetadata, None, None]:
#     return (p for p in root.rglob("metadata.json"))

app = typer.Typer()


# @app.command("autoupdate")  # type: ignore[misc]
# def autoupdate() -> None:
#
#     for p in find_metadata_files():
#         logger.info(f"Found {p}")
#         pkg = PackageMetadata.load(p)
#         logger.info(f"Loaded {pkg}")
#
#         pkg.autogenerate()


def run() -> None:
    print("RUN!")
    app()


if __name__ == "__main__":

    import cogapp

    cogapp.

    metadata_sch = PackageMetadata.Schema()
    for p in PATHS.PACKAGES_DIR.iterdir():
        metadata_json = p / FILES.METADATA_JSON
        if not metadata_json.is_file():
            continue

        meta = load_json(metadata_json, schema=metadata_sch)
        logger.info(meta.name)
        for pp in p.iterdir():
            params_json = pp / FILES.PARAMS_JSON
            if not params_json.is_file():
                continue

            params = load_json(params_json, schema=metadata_sch)
