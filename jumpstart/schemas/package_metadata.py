#!/usr/bin/env python3

# stdlib imports
import codecs
import dataclasses
from dataclasses import dataclass, field
import json
import pathlib
import typing as T

# 3rd party imports
from loguru import logger
import marshmallow as ma
from marshmallow_dataclass import NewType, add_schema


@add_schema
@dataclass(repr=False)
class PackageMetadata:
    """Holds the information from each metadata JSON file"""

    name: str
    notes: str = ""
    urls: list[str] = field(default_factory=list)
    tags: list[str] = field(default_factory=list)
    Schema: T.ClassVar[T.Type[ma.Schema]] = ma.Schema

    class Meta:
        ordered = True
        # exclude = ("metadata_path",)
        # unknown = ma.EXCLUDE

    # @classmethod
    # def load(cls, json_path: pathlib.Path) -> "PackageMetadata":
    #     with codecs.open(str(json_path), "r", encoding="utf-8", errors="ignore") as fp:
    #         data = json.load(fp)
    #         obj = cls.Schema().load(data)
    #
    #     obj.metadata_path = json_path
    #     return T.cast(PackageMetadata, obj)
    #
    # def dump(self, path: pathlib.Path) -> None:
    #     with codecs.open(str(path), "w", encoding="utf-8", errors="ignore") as fp:
    #         json.dump(
    #             self.Schema().dump(self),
    #             fp=fp,
    #             indent=2,
    #         )
