#!/usr/bin/env python3

# stdlib imports
import codecs
import dataclasses
from dataclasses import dataclass, field
import html
import json
import pathlib
import typing as T

# 3rd party imports
from loguru import logger
import marshmallow as ma
from marshmallow.fields import Field
from marshmallow_dataclass import NewType, add_schema

# 1st party imports
from jumpstart.constants import Paths

# local imports
from .fields import PathField
from .sources import Apt, Snap


@add_schema
@dataclass(repr=False)
class System:
    apt: T.Optional[Apt] = None
    snap: T.Optional[Snap] = None
    # deb: T.Optional[DebTemplateParams] = None
    # appimage: T.Optional[AppImageParams] = None
    Schema: T.ClassVar[T.Type[ma.Schema]] = ma.Schema

    class Meta:
        ordered = True
        unknown = ma.EXCLUDE

    # def __post_init__(self):


@add_schema
@dataclass(repr=False)
class PackageMetadata:
    """Holds the information from each metadata JSON file"""

    name: str = ""
    url: str = ""
    metadata_path: PathField = Paths.DEV_NULL
    tags: T.List[str] = dataclasses.field(default_factory=list)
    systems: T.List[System] = dataclasses.field(default_factory=list)
    Schema: T.ClassVar[T.Type[ma.Schema]] = ma.Schema

    class Meta:
        ordered = True
        exclude = ("metadata_path",)
        unknown = ma.EXCLUDE

    @classmethod
    def load(cls, json_path: pathlib.Path) -> "PackageMetadata":
        with codecs.open(str(json_path), "r", encoding="utf-8", errors="ignore") as fp:
            data = json.load(fp)
            obj = cls.Schema().load(data)

        obj.metadata_path = json_path
        return T.cast(PackageMetadata, obj)

    def dump(self, path: pathlib.Path) -> None:
        with codecs.open(str(path), "w", encoding="utf-8", errors="ignore") as fp:
            json.dump(
                self.Schema().dump(self),
                fp=fp,
                indent=2,
            )

    def autogenerate(self) -> None:
        for system in self.systems:
            for src in (system.apt,):
                if not src:
                    continue
                src.update()
                src.render(basepath=self.metadata_path.parent)
        self.dump(self.metadata_path)
