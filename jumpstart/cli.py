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


@app.command()  # type: ignore [misc]
def scan(
    dir: pathlib.Path = Paths.INDEX_DIR,
) -> None:

    for component_dir in sorted(dir.iterdir()):

        if not component_dir.is_dir():
            continue

        logger.info(component_dir)

        component = Component.from_path(component_dir)

        # if not component.metadata.template_params:
        #     logger.warning(component.metadata.name)
        #     continue

        if not component.alternatives:
            logger.warning(component.metadata.name)
            continue
        logger.info(component.metadata.name)
        logger.info([type(a).__name__ for a in component.alternatives])
        component.render_templates()
        component.metadata.to_path(component.metadata.json_path)  # type: ignore [arg-type]

    # typer.echo(typer.style(message, fg=rich.color.RE_COLOR))


# https://stribny.name/blog/2020/01/building-command-line-interfaces-in-python/

if __name__ == "__main__":
    app()
