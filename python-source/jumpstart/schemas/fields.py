#!/usr/bin/env python3

# stdlib imports
import pathlib
import typing as T

# 3rd party imports
from loguru import logger
from marshmallow import Schema, fields
from marshmallow.fields import Field
from marshmallow_dataclass import NewType, add_schema


class MarshmallowPathField(Field):
    """ """

    def __init__(self, *args: T.Any, **kwargs: T.Any) -> None:
        super().__init__(*args, **kwargs)

    def _serialize(self, value: pathlib.Path, *args: T.Any, **kwargs: T.Any) -> T.Optional[str]:
        if value is None:
            return None
        return str(value)

    def _deserialize(self, value: str, *args: T.Any, **kwargs: T.Any) -> T.Optional[pathlib.Path]:
        if value is None:
            return None
        return pathlib.Path(value)


# TODO validator?
PathField = NewType("PathField", pathlib.Path, field=MarshmallowPathField)
# validate=OneOf({"","edge", "classic"}))


class TrimmedString(fields.String):
    def _deserialize(self, value: T.Any, *args: T.Any, **kwargs: T.Any) -> T.Any:
        if hasattr(value, "strip"):
            value = value.strip()
        return super()._deserialize(value, *args, **kwargs)


class ArtistSchema(Schema):
    name = TrimmedString(required=True)


# https://github.com/marshmallow-code/marshmallow/issues/1391

# print(ArtistSchema().load({"name": " David "}))
