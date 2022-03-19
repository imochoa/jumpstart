#!/usr/bin/env python3

# stdlib imports
import codecs
import dataclasses
from dataclasses import dataclass, field
import html
import json
import pathlib
import typing as T

# 3rd party imports
from loguru import logger
import marshmallow as ma
from marshmallow.fields import Field
from marshmallow_dataclass import NewType, add_schema

# 1st party imports
from jumpstart.constants import Filenames

# local imports
from .templates import AltParams, SnapTemplateParams


class PathField(Field):
    """
    (De)serialization support for pathlib.Path objects while using marshmallow
            JSON-> str
            PYT -> pathlib.Path
    """

    def __init__(self: T.Any, *args: T.Any, **kwargs: T.Any) -> None:
        super().__init__(*args, **kwargs)

    def _serialize(self, value: pathlib.Path, *args: T.Any, **kwargs: T.Any) -> T.Optional[str]:
        if value is None:
            return None
        return str(value)

    def _deserialize(self, value: str, *args: T.Any, **kwargs: T.Any) -> T.Optional[pathlib.Path]:
        if value is None:
            return None
        return pathlib.Path(value)


Path = NewType("Path", object, field=PathField)


@add_schema
@dataclass
class Metadata:
    """For each Metadta JSON file, what can we expect to find"""

    json_path: Path
    name: str
    alt_params: T.List[AltParams] = dataclasses.field(
        repr=False, default_factory=list, metadata={"data_key": "alternatives"}
    )
    url: str = dataclasses.field(repr=False, default="")
    tags: T.List[str] = dataclasses.field(repr=False, default_factory=list)
    preference: T.List[str] = dataclasses.field(repr=False, default_factory=list)
    Schema: T.ClassVar[T.Type[ma.Schema]] = ma.Schema

    class Meta:
        ordered = True

    # def __post_init__(self):

    @classmethod
    def from_path(cls: T.Type["Metadata"], p: pathlib.Path) -> "Metadata":

        json_path: pathlib.Path
        if p.is_dir() and (p / f"{Filenames.metadata}.json").is_file():
            json_path = p / f"{Filenames.metadata}.json"
        elif p.is_file() and p.suffix.lower() == ".json":
            json_path = p
        else:
            raise OSError(f"Invalid path {p}")

        with codecs.open(str(json_path), "r", encoding="utf-8", errors="ignore") as fp:
            data = json.load(fp)
            data["json_path"] = json_path
            obj = cls.Schema().load(data)

        if not obj.url:
            obj.url = f"https://www.google.com/search?q={html.escape(obj.name)}"

        return T.cast("Metadata", obj)

    def to_path(self: "Metadata", p: pathlib.Path) -> None:
        json_path: Path
        if p.is_dir():
            json_path = p / f"{Filenames.metadata}.json"
        elif p.suffix.lower() == ".json":
            json_path = p
        else:
            raise OSError(f"Invalid path {p}")

        with open(json_path, "w") as fp:
            json.dump(
                obj=self.Schema(exclude=("json_path",)).dump(
                    self,
                ),
                fp=fp,
                indent=2,
            )

    # @classmethod
    # def init_kwargs(cls) -> T.List[str]:
    #     return inspect.getfullargspec(cls.__init__).args[1:]
