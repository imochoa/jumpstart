#!/usr/bin/env python3

# stdlib imports
from dataclasses import dataclass, field
import typing as T

# 3rd party imports
from loguru import logger
import marshmallow as ma
from marshmallow_dataclass import add_schema

# 1st party imports
from jumpstart.constants import PATHS

# local imports
from .fields import Path


@add_schema
@dataclass(repr=False)
class DefaultEnv:
    """
    There are system-specific defaults for each environment variable.

    You can override them here
    """

    install_dst: str = ""
    """
    DIRECTORY where
    """

    @property
    def cog_args(self) -> dict[str, str]:
        """ """
        return dict(
            INSTALL_DST=self.install_dst or "${{HOME}}/.local/bin/",
        )


@add_schema
@dataclass(repr=False)
class ParamsHeader:
    """Holds the information from each metadata JSON file"""

    template: str
    """
    Should be one of PARAMS_TYPE
    """
    priority: int = 0
    """
    Lower is higher priority
    """
    depends: list[str] = field(default_factory=list)
    """
    """
    urls: list[str] = field(default_factory=list)
    """
    """
    default_env: DefaultEnv = field(default_factory=DefaultEnv)
    """
    Overwrite defaults?
    """
    json_path: Path = PATHS.DEVNULL
    """
    Used internally to track the path to the JSON params file
    """
    # system: list[str] = field(default_factory=list)
    # """
    # """
    Schema: T.ClassVar[T.Type[ma.Schema]] = ma.Schema

    class Meta:
        ordered = True
        exclude = ("json_path",)

    def __str__(self) -> str:
        return f'<{self.__class__.__name__} template="{self.template}">'
