#!/usr/bin/env python3

# stdlib imports
from dataclasses import dataclass, field
import typing as T

# 3rd party imports
import marshmallow as ma
from marshmallow_dataclass import add_schema

# 1st party imports
from jumpstart.schemas.params_header import ParamsHeader


@add_schema
@dataclass(repr=False)
class NoParams:
    """Holds the information from each metadata JSON file"""

    header: ParamsHeader
    """
    """
    Schema: T.ClassVar[T.Type[ma.Schema]] = ma.Schema

    class Meta:
        ordered = True

    @property
    def cog_args(self) -> dict[str, str]:
        return dict()
