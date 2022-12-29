#!/usr/bin/env python3

# stdlib imports
import pathlib
import typing as T

# 3rd party imports
from loguru import logger
import marshmallow as ma
from marshmallow import ValidationError
from marshmallow.fields import Field
from marshmallow_dataclass import NewType, add_schema

#
# class PathField(Field):
#     """ """
#
#     def __init__(self, *args: T.Any, **kwargs: T.Any) -> None:
#         super().__init__(*args, **kwargs)
#
#     def _serialize(self, value: pathlib.Path, *args: T.Any, **kwargs: T.Any) -> T.Optional[str]:
#         if value is None:
#             return None
#         return str(value)
#
#     def _deserialize(self, value: str, *args: T.Any, **kwargs: T.Any) -> T.Optional[pathlib.Path]:
#         if value is None:
#             return None
#         return pathlib.Path(value)
#
#
# Path = NewType("Path", pathlib.Path, field=PathField)
# # validate=OneOf({"","edge", "classic"}))
#
#
# class TupleStrsField(ma.fields.Field):
#     """
#     equivalent to `tuple[str,...]` but required because variadic tuples are not natively supported
#     https://github.com/lovasoa/marshmallow_dataclass/issues/63
#     """
#
#     def _serialize(self, value: tuple[str, ...], attr, obj, **kwargs):
#         return value
#
#     def _deserialize(self, value, attr, data, **kwargs):
#         try:
#             return tuple(value)
#         except ValueError as error:
#             raise ValidationError("something when wrong...") from error
#
#
# TupleStrs = NewType("TupleStrs", tuple[str, ...], field=TupleStrsField)
#
#
# class TrimmedString(ma.fields.String):
#     """
#     Take care of leading trailing spaces
#     """
#
#     def _deserialize(self, value: T.Any, *args: T.Any, **kwargs: T.Any) -> T.Any:
#         if hasattr(value, "strip"):
#             value = value.strip()
#         return super()._deserialize(value, *args, **kwargs)
