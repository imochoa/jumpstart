#!/usr/bin/env python3

# stdlib imports
from dataclasses import dataclass, field
import typing as T

# 3rd party imports
import marshmallow as ma
from marshmallow_dataclass import add_schema

# 1st party imports
from jumpstart.constants import PATHS

# local imports
from .fields import Path


@add_schema
@dataclass(repr=False)
class PackageMetadata:
    """Holds the information from each metadata JSON file"""

    name: str
    """
    """
    urls: list[str] = field(default_factory=list)
    """
    """
    tags: list[str] = field(default_factory=list)
    """
    """
    description: str = ""
    """
    """
    json_path: Path = PATHS.DEVNULL
    """
    Used internally to track the path to the JSON params file
    """
    Schema: T.ClassVar[T.Type[ma.Schema]] = ma.Schema

    class Meta:
        ordered = True
        exclude = ("json_path",)

    @ma.pre_dump
    def set_defaults(self, in_data: "PackageMetadata", **kwargs: T.Any) -> "PackageMetadata":
        # Set name from filepath, if missing
        if not in_data.name and in_data.json_path.is_file():
            in_data.name = in_data.json_path.parent.name
        # Set URL to google search, if missing
        return in_data

    def __str__(self) -> str:
        return f'<{self.__class__.__name__} name="{self.name}">'
