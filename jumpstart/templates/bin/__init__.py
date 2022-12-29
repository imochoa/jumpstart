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
class BinParams:
    """Holds the information from each metadata JSON file"""

    header: ParamsHeader
    """
    Should be one of....
    """
    orgrepo: str = ""
    """
    For installing from a github release
    Should be in the shape of organization/repository
    """
    # src:str = ""
    # """
    # """
    Schema: T.ClassVar[T.Type[ma.Schema]] = ma.Schema

    class Meta:
        ordered = True

    @property
    def cog_args(self) -> list[str]:
        return [
            "-D",
            f"ORGREPO={self.orgrepo}",
        ]
