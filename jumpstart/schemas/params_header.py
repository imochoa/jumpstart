#!/usr/bin/env python3

# stdlib imports
from dataclasses import dataclass, field
import typing as T

# 3rd party imports
import marshmallow as ma
from marshmallow_dataclass import add_schema


@add_schema
@dataclass(repr=False)
class ParamsHeader:
    """Holds the information from each metadata JSON file"""

    template: str
    """
    Should be one of....
    """
    depends: list[str] = field(default_factory=list)
    # system: list[str] = field(default_factory=list)
    Schema: T.ClassVar[T.Type[ma.Schema]] = ma.Schema

    class Meta:
        ordered = True
