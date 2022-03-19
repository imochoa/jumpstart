#!/usr/bin/env python3

# stdlib imports
from dataclasses import dataclass, field
import pathlib
import typing as T

# 3rd party imports
from loguru import logger
import marshmallow as ma
from marshmallow.fields import Field
from marshmallow_dataclass import NewType, add_schema


class SnapPolicyField(Field):
    """
    (De)serialization support for snap policies
            JSON-> str
            PYT -> pathlib.Path
    """

    def __init__(self: T.Any, *args: T.Any, **kwargs: T.Any) -> None:
        super().__init__(*args, **kwargs)

    def _serialize(self, value: pathlib.Path, *args: T.Any, **kwargs: T.Any) -> str:
        if value is None:
            return ""
        return str(value)

    def _deserialize(self, value: str, *args: T.Any, **kwargs: T.Any) -> str:
        if not value:
            return ""
        value = value.strip().lower()
        if not value.startswith("--"):
            prefix = ""
            for idx in range(2):
                if value[idx] != "-":
                    prefix += "-"
            value = f"{prefix}{value}"
        assert value in {
            "",
            "--edge",
            "--classic",
        }, f"Unknown SNAP policy: {value}"
        return value


SnapPolicy = NewType("SnapPolicy", str, field=SnapPolicyField)


@add_schema
@dataclass
class SnapTemplateParams:
    """JSON Parameters required to fill in the Snap templates"""

    pkg: str = field(default="")
    policy: SnapPolicy = field(default="")
    Schema: T.ClassVar[T.Type[ma.Schema]] = ma.Schema

    class Meta:
        ordered = True
