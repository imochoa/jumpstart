#!/usr/bin/env python3

# stdlib imports
import functools
import os
import pathlib
import sys
from types import SimpleNamespace
import typing as T

# 3rd party imports
import jinja2


class Paths(SimpleNamespace):
    PKG_DIR: T.Final[pathlib.Path] = pathlib.Path(__file__).parent
    PY_SOURCE_DIR: T.Final[pathlib.Path] = (PKG_DIR / "..").resolve()
    REPO_DIR: T.Final[pathlib.Path] = (PY_SOURCE_DIR / "..").resolve()
    INDEX_DIR: T.Final[pathlib.Path] = PKG_DIR / "pkg-index"
    TEST_DIR: T.Final[pathlib.Path] = REPO_DIR / "test"
    TEMPLATE_DIR: T.Final[pathlib.Path] = PKG_DIR / "templates"
    DEV_NULL: T.Final[pathlib.Path] = pathlib.Path(os.devnull)


class Names(SimpleNamespace):
    """
    Accepted filenames for each installable. The extensions are usually ".sh"
    """

    install: T.Final[str] = "install"
    setup: T.Final[str] = "setup"
    update: T.Final[str] = "update"
    remove: T.Final[str] = "remove"
    status: T.Final[str] = "status"
    version: T.Final[str] = "version"
    metadata: T.Final[str] = "metadata"
    default_dir: T.Final[str] = "default"


template_loader: T.Final[T.Any] = jinja2.FileSystemLoader(searchpath=Paths.TEMPLATE_DIR)
template_env = jinja2.Environment(loader=template_loader, autoescape=True)
