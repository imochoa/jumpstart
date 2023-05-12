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
    """
    package: str
    """
    From PYPI
    cmake

    From source
    pipx install git+https://github.com/psf/black.git
    pipx install git+https://github.com/psf/black.git@branch  # branch of your choice
    pipx install git+https://github.com/psf/black.git@ce14fa8b497bae2b50ec48b3bd7022573a59cdb1  # git hash
    pipx install https://github.com/psf/black/archive/18.9b0.zip  # install a release

    """
    app: str = ""
    """
    python package to run/install (in case there are several)
    """
    ver: str = ""
    """
    Force installing a specific version (eg. 1.0.0)
    """
    Schema: T.ClassVar[T.Type[ma.Schema]] = ma.Schema

    class Meta:
        ordered = True

    @property
    def cog_args(self) -> dict[str, str]:
        """ """
        return dict(
            PACKAGE=self.package,
            APP=self.app,
            VER=self.ver,
        )
