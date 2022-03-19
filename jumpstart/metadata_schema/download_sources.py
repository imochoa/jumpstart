#!/usr/bin/env python3

# stdlib imports
from dataclasses import dataclass, field
import pathlib
import typing as T

# 3rd party imports
from loguru import logger
import marshmallow as ma
from marshmallow_dataclass import add_schema

# local imports
from .sys_context import SystemContext


@add_schema
@dataclass(order=True)
class GithubRelease:
    """For downloading from a github release"""

    user: str = field(default="")
    repo: str = field(default="")
    filter_args: T.List[str] = field(default_factory=list)
    Schema: T.ClassVar[T.Type[ma.Schema]] = ma.Schema


@add_schema
@dataclass(order=True)
class DownloadSource:
    """"""

    static_url: str = field(default="")
    github: T.Optional[GithubRelease] = None
    url: str = field(default="", metadata=dict(data_key="url_post_resolution"))
    Schema: T.ClassVar[T.Type[ma.Schema]] = ma.Schema
    # class Meta:
    #     exclude = ('url',)

    def __post_init__(self: "DownloadSource") -> None:
        """
        1. Perform safety checks
        2. Determine self.url attribute automatically based on the other attributes
        """

        if self.static_url:

            # TODO cleanups! strip http:// and re-add it!
            # self.static_url = urllib.parse.quote(self.static_url)
            # TODO SHell escape as wellAlternative!
            self.url = self.static_url
