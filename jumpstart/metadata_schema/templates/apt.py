#!/usr/bin/env python3

# stdlib imports
from dataclasses import dataclass, field
import typing as T

# 3rd party imports
from loguru import logger
import marshmallow as ma
from marshmallow_dataclass import add_schema


@add_schema
@dataclass
class AptTemplateParams:
    """JSON Parameters required to fill in the Apt templates"""

    pkgs: T.List[str] = field(default_factory=list)
    ppas: T.List[str] = field(default_factory=list)
    Schema: T.ClassVar[T.Type[ma.Schema]] = ma.Schema

    class Meta:
        ordered = True
