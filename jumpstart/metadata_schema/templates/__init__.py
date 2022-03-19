#!/usr/bin/env python3

# stdlib imports
from dataclasses import dataclass, field
import pathlib
import typing as T

# 3rd party imports
from loguru import logger
import marshmallow as ma
from marshmallow_dataclass import NewType, add_schema

# 1st party imports
from jumpstart.metadata_schema.sys_context import SystemContext

# local imports
from .apt import AptTemplateParams
from .deb import DebTemplateParams
from .snap import SnapTemplateParams


@add_schema
@dataclass
class AltParams:
    system_context: SystemContext = field(default=SystemContext.any(), metadata=dict(data_key="system"))
    apt: T.Optional[AptTemplateParams] = None
    snap: T.Optional[SnapTemplateParams] = None
    deb: T.Optional[DebTemplateParams] = None
    Schema: T.ClassVar[T.Type[ma.Schema]] = ma.Schema

    class Meta:
        ordered = True

    @ma.post_dump
    def remove_skip_values(self: "AltParams", data: T.Dict[str, T.Any], **kwargs: T.Any) -> T.Dict[str, T.Any]:
        """Ignore empty fields"""
        return {key: value for key, value in data.items() if value is not None}
