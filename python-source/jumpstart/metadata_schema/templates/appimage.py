#!/usr/bin/env python3

# stdlib imports
from dataclasses import dataclass, field
import typing as T

# 3rd party imports
from loguru import logger
import marshmallow as ma
from marshmallow_dataclass import add_schema
from jumpstart.metadata_schema.download_sources import DownloadSource


@add_schema
@dataclass
class AppImageParams:
    """JSON Parameters required to fill in the Apt templates"""

    download_source: DownloadSource
    Schema: T.ClassVar[T.Type[ma.Schema]] = ma.Schema

    class Meta:
        ordered = True
