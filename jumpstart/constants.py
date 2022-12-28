#!/usr/bin/env python3

# stdlib imports
from pathlib import Path
import tempfile
from types import SimpleNamespace
import typing as T


class PATHS(SimpleNamespace):
    TMP: T.Final[Path] = Path(tempfile.gettempdir())
    PYPKG_DIR: T.Final[Path] = Path(__file__).parent.resolve()
    TEMPLATES_DIR: T.Final[Path] = PYPKG_DIR / "templates"
    REPO_DIR: T.Final[Path] = PYPKG_DIR.parent
    PACKAGES_DIR: T.Final[Path] = REPO_DIR / "packages"


class SCRIPTS(SimpleNamespace):
    INSTALL: T.Final[str] = "install"
    REMOVE: T.Final[str] = "remove"
    LOCAL_VER: T.Final[str] = "local-ver"
    UPSTREAM_VER: T.Final[str] = "upstream-ver"
    SETUP: T.Final[str] = "setup"
    UPDATE: T.Final[str] = "update"

    @classmethod
    def as_set(cls) -> set[str]:
        return {v for k, v in cls.__dict__.items() if k.isupper()}


class FILES(SimpleNamespace):
    """ """

    METADATA_JSON: T.Final[str] = "metadata.json"
    PARAMS_JSON: T.Final[str] = "params.json"
    CONFIG_JSON: T.Final[str] = "config.json"


class System(T.NamedTuple):
    """
    Relevant someday...
    """

    plat: str
    """
    Platform (linux, max, windows)
    """
    os: str
    """
    Operating System (ubuntu 20.04, ubuntu 22.04)
    """
    arch: str
    """
    Architecture (ARM, x86, x64)
    """
