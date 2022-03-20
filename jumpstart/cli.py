#!/usr/bin/env python3

# stdlib imports
import pathlib

# 3rd party imports
from loguru import logger
import rich.color
import typer

# 1st party imports
from jumpstart.constants import Paths
from jumpstart.core import Component

app = typer.Typer()


@app.command("scan")  # type: ignore [misc]
def scan(
    dir: pathlib.Path = Paths.INDEX_DIR,
    debug: bool = False,
) -> None:

    all_components = Component.from_index_dir(
        dir,
        debug=debug,
    )

    for component in all_components:
        component.render_templates()
        component.metadata.to_path(component.metadata.json_path)  # type: ignore [arg-type]


@app.command("list")  # type: ignore [misc]
def list(
    dir: pathlib.Path = Paths.INDEX_DIR,
    debug: bool = False,
) -> None:
    all_components = Component.from_index_dir(
        dir,
        debug=debug,
    )

    for component in all_components:
        component.render_templates()
        component.metadata.to_path(component.metadata.json_path)  # type: ignore [arg-type]


def main() -> None:
    app()


if __name__ == "__main__":
    main()
