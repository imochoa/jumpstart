#!/usr/bin/env python3

# stdlib imports
from dataclasses import dataclass, field
import typing as T

# 3rd party imports
from loguru import logger
import marshmallow as ma
from marshmallow_dataclass import add_schema

# 1st party imports
from jumpstart.metadata_schema.download_sources import DownloadSource

if T.TYPE_CHECKING:
    # 1st party imports
    from jumpstart.metadata_schema.sys_context import SystemContext


@add_schema
@dataclass
class DebTemplateParams:
    """

    JSON Parameters required to fill in the Deb templates

    Looking for packages: apt-cache search


    """

    src: DownloadSource
    name: str = ""  #: name used to uninstall the .deb : 'sudo apt remove -y {{name}}'. If missing, it will be taken from the metadata
    Schema: T.ClassVar[T.Type[ma.Schema]] = ma.Schema

    class Meta:
        ordered = True

    @ma.post_dump
    def remove_skip_values(self: "DebTemplateParams", data: T.Dict[str, T.Any], **kwargs: T.Any) -> T.Dict[str, T.Any]:
        """Ignore empty/any fields"""
        return {key: value for key, value in data.items() if value}
