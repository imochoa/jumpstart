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
from jumpstart.constants import Paths
from jumpstart.schemas import PackageMetadata

# from jumpstart.core import Component


def iter_packages() -> T.Generator[PackageMetadata, None, None]:
    return (PackageMetadata.load(p) for p in Paths.INDEX_DIR.rglob("metadata.json"))


app = typer.Typer()
#
# @app.command("tree")  # type: ignore[misc]
# def tree(
#         dir: pathlib.Path = Paths.INDEX_DIR,
#         debug: bool = False,
# ) -> None:
#     """Tree of available programs & alternatives"""
#
#     #             style = "dim" if path.name.startswith("__") else ""
#     #             branch = tree.add(
#     #                 f"[bold magenta]:open_file_folder: [link file://{path}]{escape(path.name)}",
#     #                 style=style,
#     #                 guide_style=style,
#     #             )
#     tree = Tree(
#         f":open_file_folder: [link file://{dir}]{dir}",
#         guide_style="bold bright_blue",
#     )
#
#     for component in Component.from_index_dir(
#             dir,
#             debug=debug,
#     ):
#
#         # Branch
#         # style = "dim" if path.name.startswith("__") else ""
#         style = ""
#         branch_dir = component.metadata.json_path.parent
#         branch = tree.add(
#             f"[bold magenta]:open_file_folder: [link file://{branch_dir}]{escape(branch_dir.name)}",
#             style=style,
#             guide_style=style,
#         )
#         for alt in component.alternatives:
#             branch.add(Text(alt.out_dir.name))
#
#         # path  =component.metadata.json_path
#         # text_filename = Text(component.metadata.name, "green")
#         # text_filename.highlight_regex(r"\..*$", "bold red")
#         # text_filename.stylize(f"link file://{path}")
#         # file_size = path.stat().st_size
#         # text_filename.append(f" ({decimal(file_size)})", "blue")
#         # # icon = "🐍 " if path.suffix == ".py" else "📄 "
#         # icon = "📄 "
#         # tree.add(Text(icon) + text_filename)
#         # component.render_templates()
#         # component.metadata.to_path(component.metadata.json_path)  # type: ignore[arg-type]
#     rich.print(tree)
#
# @app.command("table")  # type: ignore[misc]
# def table(
#         dir: pathlib.Path = Paths.INDEX_DIR,
#         debug: bool = False,
# ) -> None:
#     from rich.console import Console
#     from rich.table import Table
#
#     console = Console()
#
#     table = Table(show_header=True, header_style="bold magenta")
#     table.add_column("Date", style="dim", width=12)
#     table.add_column("Title")
#     table.add_column("Production Budget", justify="right")
#     table.add_column("Box Office", justify="right")
#     table.add_row(
#         "Dec 20, 2019", "Star Wars: The Rise of Skywalker", "$275,000,000", "$375,126,118"
#     )
#     table.add_row(
#         "May 25, 2018",
#         "[red]Solo[/red]: A Star Wars Story",
#         "$275,000,000",
#         "$393,151,347",
#     )
#     table.add_row(
#         "Dec 15, 2017",
#         "Star Wars Ep. VIII: The Last Jedi",
#         "$262,000,000",
#         "[bold]$1,332,539,889[/bold]",
#     )
#
#     console.print(table)
#
#
#     # for component in Component.from_index_dir(
#     #         dir,
#     #         debug=debug,
#     # ):
#     #     component.render_templates()
#     #     component.metadata.to_path(component.metadata.json_path)  # type: ignore[arg-type]


@app.command("autoupdate")  # type: ignore[misc]
def autoupdate() -> None:

    for pkg in iter_packages():
        pkg.autogenerate()
        print(pkg)

    # for component in Component.from_index_dir(
    #     dir,
    #     debug=debug,
    # ):
    #     component.render_templates()
    #     component.metadata.to_path(component.metadata.json_path)  # type: ignore[arg-type]


#
# @app.command("list")  # type: ignore[misc]
# def list(
#     dir: pathlib.Path = Paths.INDEX_DIR,
#     debug: bool = False,
# ) -> None:
#     all_components = Component.from_index_dir(
#         dir,
#         debug=debug,
#     )
#
#     for component in all_components:
#         component.render_templates()
#         component.metadata.to_path(component.metadata.json_path)  # type: ignore [arg-type]


def main() -> None:
    app()


if __name__ == "__main__":
    # tree()
    autoupdate()
    main()
