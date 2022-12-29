#!/usr/bin/env python3

# stdlib imports
from dataclasses import dataclass, field
import typing as T

# 3rd party imports
import marshmallow as ma
from marshmallow_dataclass import add_schema


@add_schema
@dataclass(repr=False)
class PackageMetadata:
    """Holds the information from each metadata JSON file"""

    name: str
    urls: list[str] = field(default_factory=list)
    tags: list[str] = field(default_factory=list)
    description: str = ""
    Schema: T.ClassVar[T.Type[ma.Schema]] = ma.Schema

    class Meta:
        ordered = True
        # exclude = ("metadata_path",)
        # unknown = ma.EXCLUDE
