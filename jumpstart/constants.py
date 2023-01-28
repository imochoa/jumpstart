#!/usr/bin/env python3
# stdlib imports
import os
from pathlib import Path
import tempfile
from types import SimpleNamespace
import typing as T


class PATHS(SimpleNamespace):
    """
    All relevant pathlib.Path paths
    """

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
    Top-level directory where the packages are stored
    """


class SCRIPTS(SimpleNamespace):
    """
    Filename of the templates
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
    """
    Namespace to hold file & directory names
    """

    METADATA_JSON: T.Final[str] = "metadata.json"
    """
    General information about a package
    """
    PARAMS_JSON: T.Final[str] = "params.json"
    """
    Parameters required for each template type
    """
    CONFIG_JSON: T.Final[str] = "config.json"
    """
    TODO
    configure the installation (install paths, local/global installations, prefer apt, etc.)
    """
    DATA_DIR: T.Final[str] = "data"
    """
    Directory to store extra data
    """
    POST_DIR: T.Final[str] = ".post"
    """
    Templates to run AFTER & append to the default ones' outputs
    """
    PRE_DIR: T.Final[str] = ".pre"
    """
    TODO
    Templates to run BEFORE & prepend to the default ones' outputs
    """


class ARCHIVE_EXTS(SimpleNamespace):
    """ """

    ZIP: T.Final[tuple[str, ...]] = (".zip",)
    """
    """
    TAR: T.Final[tuple[str, ...]] = (".tar",)
    """
    """
    TARGZ: T.Final[tuple[str, ...]] = (
        ".tar.gz",
        ".tar.xz",
    )
    """
    """
    GZ: T.Final[tuple[str, ...]] = (".gz",)
    """
    """
    SEVENZ: T.Final[tuple[str, ...]] = (".7z",)
    """
    """

    @classmethod
    def match(cls, path: str) -> str:
        """
        *path* can be either a file path or a URL
        returns the name of the key!
        """
        known_extmap = {v: k for k, v in cls.__dict__.items() if isinstance(v, tuple)}
        known_exts = sorted(known_extmap, reverse=True)
        for exts in known_exts:
            if any(path.lower().endswith(ext.lower()) for ext in exts):
                return known_extmap[exts]
        raise KeyError(f"No known archive extension for {path}")


class System(T.NamedTuple):
    """
    TODO Relevant someday...
    System information required by the packages
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
