#!/usr/bin/env python3

# stdlib imports
from dataclasses import dataclass, field
from pathlib import Path
import typing as T

# 3rd party imports
import marshmallow as ma
from marshmallow_dataclass import add_schema

# 1st party imports
from jumpstart.constants import PATHS


@add_schema
@dataclass(repr=False)
class ParamsHeader:
    """Holds the information from each metadata JSON file"""

    template: str
    """
    Should be one of PARAMS_TYPE
    """
    priority: int = 0
    """
    Lower is higher priority
    """
    depends: list[str] = field(default_factory=list)
    """
    """
    urls: list[str] = field(default_factory=list)
    """
    """
    json_path: Path = PATHS.DEVNULL
    """
    Used internally to track the path to the JSON params file
    """
    # system: list[str] = field(default_factory=list)
    # """
    # """
    Schema: T.ClassVar[T.Type[ma.Schema]] = ma.Schema

    class Meta:
        ordered = True
        exclude = ("json_path",)
