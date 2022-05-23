#!/usr/bin/env python3

# stdlib imports
import functools
import sys
import os
import pathlib
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
template_env = jinja2.Environment(loader=template_loader)

KNOWN_TEMPLATES: T.Dict["Filename", T.Dict["Filename", jinja2.Template]] = dict()
aux_d: T.Dict["Filename", jinja2.Template]
for d in (d for d in Paths.TEMPLATE_DIR.iterdir() if d.is_dir()):
    key = Filename(d.name.lower().strip())
    aux_d = dict()
    for f in (f for f in d.iterdir() if f.is_file() and f.suffix.lower() == ".j2"):
        aux_d[Filename(f.stem)] = template_env.get_template(str(f.relative_to(Paths.TEMPLATE_DIR)))
    KNOWN_TEMPLATES[key] = aux_d
del aux_d
