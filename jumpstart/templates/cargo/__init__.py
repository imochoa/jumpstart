#!/usr/bin/env python3

# stdlib imports
from dataclasses import dataclass, field
import json
import typing as T

# 3rd party imports
import marshmallow as ma
from marshmallow_dataclass import add_schema

# 1st party imports
from jumpstart.schemas.params_header import ParamsHeader
from jumpstart.schemas.pkg_download import PkgDownloadSources
from jumpstart.schemas.schema_utils import dump_json


@add_schema
@dataclass(repr=False)
class CargoParams:
    """
    For one executable file
    """

    header: ParamsHeader
    """
    Should be one of....
    """

    Schema: T.ClassVar[T.Type[ma.Schema]] = ma.Schema

    class Meta:
        ordered = True

    @property
    def cog_args(self) -> dict[str, str]:
        return dict()
