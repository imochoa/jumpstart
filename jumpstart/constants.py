#!/usr/bin/env python3
# stdlib imports
import os
from pathlib import Path
import tempfile
from types import SimpleNamespace
import typing as T


class PATHS(SimpleNamespace):
    """ """

    TMP: T.Final[Path] = Path(tempfile.gettempdir())
    """
    OS Temporary directory
    """
    DEVNULL: T.Final[Path] = Path(os.devnull)
    """
    """
    PYPKG_DIR: T.Final[Path] = Path(__file__).parent.resolve()
    """
    Top-level python package
    """
    TEMPLATES_DIR: T.Final[Path] = PYPKG_DIR / "templates"
    """
    Python package containing the templates
    """
    REPO_DIR: T.Final[Path] = PYPKG_DIR.parent
    """
    GitHub repository
    """
    PACKAGES_DIR: T.Final[Path] = REPO_DIR / "packages"
    """
    """


class SCRIPTS(SimpleNamespace):
    """
    Templated scripts
    """

    INSTALL: T.Final[str] = "install"
    """
    """
    REMOVE: T.Final[str] = "remove"
    """
    """
    LOCAL_VER: T.Final[str] = "local-ver"
    """
    """
    UPSTREAM_VER: T.Final[str] = "upstream-ver"
    """
    """
    UPDATE: T.Final[str] = "update"
    """
    """
    # SETUP: T.Final[str] = "setup"
    # """
    # """

    @classmethod
    def as_set(cls) -> set[str]:
        return {v for k, v in cls.__dict__.items() if k.isupper()}


class FILES(SimpleNamespace):
    """ """

    METADATA_JSON: T.Final[str] = "metadata.json"
    """
    """
    PARAMS_JSON: T.Final[str] = "params.json"
    """
    """
    CONFIG_JSON: T.Final[str] = "config.json"
    """
    """
    DATA_DIR: T.Final[str] = "data"
    """
    """
    POST_DIR: T.Final[str] = ".post"
    """
    """


class ENVVARS(SimpleNamespace):
    """
    INSTALLDIR=/usr/local/bin
    """

    INSTALL_P: T.Final[str] = "INSTALL_DST"
    """
    INSTALLDIR = / usr / local / bin
    # Single-user
    INSTALLDIR = ~ /.local / bin /
    """
    FONT_P: T.Final[str] = "FONT_DST"
    """
    """
    WALLPAPER_P: T.Final[str] = "FONT_DST"
    """
    """
    BASHCOMP_P: T.Final[str] = "BASHCOMP_P"
    """
    =${BASHCOMP:-${HOME}/.config/bash/bash_completion}
    """
    ZSHCOMP_D: T.Final[str] = "ZSHCOMP_D"
    """
    =${ZSHCOMP:-${HOME}/.config/zsh/completions}
    """


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
