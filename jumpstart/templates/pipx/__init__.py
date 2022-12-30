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
class PipxParams:
    """Holds the information from each metadata JSON file"""

    header: ParamsHeader
    """
    Should be one of....
    """
    url: str
    """
    """
    Schema: T.ClassVar[T.Type[ma.Schema]] = ma.Schema

    class Meta:
        ordered = True

    @property
    def cog_args(self) -> dict[str, str]:
        # pkg_str = ",".join(self.pkgs) or '""'
        # ppa_str = ",".join(self.ppas) or '""'
        # return ["-D", f"PKGS={pkg_str}", "-D", f"PPAS={ppa_str}"]
        return dict()
