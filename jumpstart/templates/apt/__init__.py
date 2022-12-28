#!/usr/bin/env python3

# stdlib imports
from dataclasses import dataclass, field
import typing as T

# 3rd party imports
import marshmallow as ma
from marshmallow_dataclass import add_schema
from jumpstart.schemas.params_header import ParamsHeader

@add_schema
@dataclass(repr=False)
class AptParams:
    """Holds the information from each metadata JSON file"""

    header:ParamsHeader
    """
    Should be one of....
    """
    pkgs: list[str] = field(default_factory=list)
    ppas: list[str] = field(default_factory=list)
    """
    PPAS HAVE TO START WITH ppa: -> validate it!
    """
    Schema: T.ClassVar[T.Type[ma.Schema]] = ma.Schema
    class Meta:
        ordered = True

