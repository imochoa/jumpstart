#!/usr/bin/env python3

# stdlib imports
from pathlib import Path
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
from jumpstart.schemas import PackageMetadata, dump_json, load_json
from jumpstart.templates import PARAMS_TYPE, cog_param, get_param_schema

app = typer.Typer()


def loop_over_pkg_jsons(
    package_dir: Path = PATHS.PACKAGES_DIR,
) -> T.Generator[tuple[Path, tuple[Path, ...]], None, None]:
    """
    For each package in *package_dir* yields:
        (package_metadata1.json, (apt_params1.json, apt_params2.json, flatpak_params1.json))
        (package_metadata2.json, (apt_paramsA.json, flatpak_paramsA.json, flatpak_paramsB.json))
    """
    for p in package_dir.iterdir():
        m_json = p / FILES.METADATA_JSON
        if not m_json.is_file():
            continue
        param_jsons_gen = (pp / FILES.PARAMS_JSON for pp in p.iterdir())
        param_jsons = tuple(p for p in param_jsons_gen if p.is_file())
        if any(param_jsons):
            yield (m_json, param_jsons)


def loop_over_pkgs(
    package_dir: Path = PATHS.PACKAGES_DIR,
) -> T.Generator[tuple[PackageMetadata, tuple[PARAMS_TYPE, ...]], None, None]:
    """
    For each package in *package_dir* yields:
        (package_metadata1.json, (apt_params1.json, apt_params2.json, flatpak_params1.json))
        (package_metadata2.json, (apt_paramsA.json, flatpak_paramsA.json, flatpak_paramsB.json))
    """
    m_sch = PackageMetadata.Schema()
    for metadata_json, param_jsons in loop_over_pkg_jsons(package_dir):
        meta = m_sch.load(load_json(metadata_json))
        meta.json_path = metadata_json
        params: list[PARAMS_TYPE] = []
        for param_json in param_jsons:
            p_sch = get_param_schema(param_json).Schema()
            p_obj = p_sch.load(load_json(param_json))
            p_obj.header.json_path = param_json
            params.append(p_obj)
        if params:
            yield (meta, tuple(params))


def validate_schemas(
    package_dir: Path = PATHS.PACKAGES_DIR,
    reexport: bool = True,
) -> None:
    """
    Look up all paths at *package_dir* and try to validate them
    """

    m_sch = PackageMetadata.Schema()
    for metadata_json, param_jsons in loop_over_pkg_jsons(package_dir):
        m_obj = load_json(metadata_json)
        m_sch.validate(m_obj)
        if reexport:
            meta = m_sch.load(m_obj)
            meta.json_path = metadata_json
            dump_json(metadata_json, obj=m_sch.dump(meta))
        for param_json in param_jsons:
            p_sch = get_param_schema(param_json).Schema()
            p_obj = load_json(param_json)
            p_sch.validate(p_obj)
            if reexport:
                p = p_sch.load(p_obj)
                p.header.json_path = param_json
                dump_json(param_json, obj=p_sch.dump(p))


def run() -> None:
    print("RUN!")
    app()


if __name__ == "__main__":
    packages_dir = PATHS.PACKAGES_DIR
    validate_schemas(packages_dir, reexport=True)
    #
    # for metadata, params in loop_over_pkgs(packages_dir,):
    #     logger.info(metadata)
    #     for param in params:
    #         logger.debug(param)
    #         cog_param(param)
