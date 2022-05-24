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


Filename = T.NewType("Filename", str)


class Filenames(SimpleNamespace):
    """
    Accepted filenames for each installable. The extensions are usually ".sh"
    """

    install = Filename("install")
    setup = Filename("setup")
    update = Filename("update")
    remove = Filename("remove")
    status = Filename("status")
    version = Filename("version")
    metadata = Filename("metadata")

    @classmethod
    @functools.lru_cache()
    def as_set(cls) -> T.Set["Filename"]:
        return {Filename(s) for s in cls.__dict__.keys() if not s.startswith("__")}


template_loader: T.Final[T.Any] = jinja2.FileSystemLoader(searchpath=Paths.TEMPLATE_DIR)
template_env = jinja2.Environment(loader=template_loader, autoescape=True)
