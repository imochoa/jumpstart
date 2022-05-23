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

from jumpstart.constants import Paths
from jumpstart.schemas.fields import PathField

from .apt import Apt
from .fields import PathField

@add_schema
@dataclass(repr=False)
class System:
    apt: T.Optional[Apt] = None
    # snap: T.Optional[SnapTemplateParams] = None
    # deb: T.Optional[DebTemplateParams] = None
    # appimage: T.Optional[AppImageParams] = None
    class Meta:
        ordered = True
        unknown = ma.EXCLUDE

    # def __post_init__(self):



@add_schema
@dataclass(repr=False)
class PackageMetadata:
    """Holds the information from each metadata JSON file"""
    name: str = ""
    url: str = ""
    metadata_path: PathField = Paths.DEV_NULL
    tags: T.List[str] = dataclasses.field(default_factory=list)
    systems: T.List[System] = dataclasses.field(default_factory=list)
    # Schema: T.ClassVar[T.Type[ma.Schema]] = ma.Schema

    class Meta:
        ordered = True
        exclude=('metadata_path',)
        unknown = ma.EXCLUDE

    @classmethod
    def load(cls,json_path:pathlib.Path):
        with codecs.open(str(json_path), "r", encoding="utf-8", errors="ignore") as fp:
            data = json.load(fp)
            obj = cls.Schema().load(data)

        obj.metadata_path =json_path
        return obj

    def dump(self,path:pathlib.Path):
        with codecs.open(str(path), "w", encoding="utf-8", errors="ignore") as fp:
            json.dump(self.Schema().dump(self),fp=fp,indent=2)
            # data["json_path"] = json_path
            # obj = json.dump(self.Schema().dump(data),obj=
        # return obj


    def autogenerate(self):
        for system in self.systems:
            for src in (system.apt,):
                if not src:
                    continue
                src.update()
                src.render(metadata_path=self.metadata_path)
        self.dump(self.metadata_path)

    # @classmethod
    # def from_dir(cls, dir_path: pathlib.Path) -> T.Self:
    #
    #     if not dir_path.is_dir():
    #         raise OSError(f"{dir_path} was not a directory!")
    #     metadata_json = dir_path/f"{Filenames.metadata}.json"
    #     if not metadata_json.is_file():
    #         raise OSError(f"{metadata_json} did not exist!")
    #
    #
    #
    #     json_path: pathlib.Path
    #     if p.is_dir() and (p / f"{Filenames.metadata}.json").is_file():
    #         json_path = p / f"{Filenames.metadata}.json"
    #     elif p.is_file() and p.suffix.lower() == ".json":
    #         json_path = p
    #     else:
    #         raise OSError(f"Invalid path {p}")
    #
    #     with codecs.open(str(json_path), "r", encoding="utf-8", errors="ignore") as fp:
    #         data = json.load(fp)
    #         data["json_path"] = json_path
    #         obj = cls.Schema().load(data)
    #
    #     if not obj.url:
    #         obj.url = f"https://www.google.com/search?q={html.escape(obj.name)}"
    #
    #     return T.cast("Metadata", obj)
    #
    # def to_path(self: "Metadata", p: pathlib.Path) -> None:
    #     json_path: Path
    #     if p.is_dir():
    #         json_path = p / f"{Filenames.metadata}.json"
    #     elif p.suffix.lower() == ".json":
    #         json_path = p
    #     else:
    #         raise OSError(f"Invalid path {p}")
    #
    #     with open(json_path, "w") as fp:
    #         json.dump(
    #             obj=self.Schema(exclude=("json_path",)).dump(
    #                 self,
    #             ),
    #             fp=fp,
    #             indent=2,
    #         )

    # @classmethod
    # def init_kwargs(cls) -> T.List[str]:
    #     return inspect.getfullargspec(cls.__init__).args[1:]

# @add_schema
# @dataclass
# class Metadata:
#     """For each Metadata JSON file, what can we expect to find"""
#
#     json_path: Path
#     name: str
#     alt_params: T.List[AltParams] = dataclasses.field(
#         repr=False, default_factory=list, metadata={"data_key": "alternatives"}
#     )
#     url: str = dataclasses.field(repr=False, default="")
#     tags: T.List[str] = dataclasses.field(repr=False, default_factory=list)
#     preference: T.List[str] = dataclasses.field(repr=False, default_factory=list)
#     Schema: T.ClassVar[T.Type[ma.Schema]] = ma.Schema
#
#     class Meta:
#         ordered = True
#
#     # def __post_init__(self):
#
#     @classmethod
#     def from_path(cls: T.Type["Metadata"], p: pathlib.Path) -> "Metadata":
#
#         json_path: pathlib.Path
#         if p.is_dir() and (p / f"{Filenames.metadata}.json").is_file():
#             json_path = p / f"{Filenames.metadata}.json"
#         elif p.is_file() and p.suffix.lower() == ".json":
#             json_path = p
#         else:
#             raise OSError(f"Invalid path {p}")
#
#         with codecs.open(str(json_path), "r", encoding="utf-8", errors="ignore") as fp:
#             data = json.load(fp)
#             data["json_path"] = json_path
#             obj = cls.Schema().load(data)
#
#         if not obj.url:
#             obj.url = f"https://www.google.com/search?q={html.escape(obj.name)}"
#
#         return T.cast("Metadata", obj)
#
#     def to_path(self: "Metadata", p: pathlib.Path) -> None:
#         json_path: Path
#         if p.is_dir():
#             json_path = p / f"{Filenames.metadata}.json"
#         elif p.suffix.lower() == ".json":
#             json_path = p
#         else:
#             raise OSError(f"Invalid path {p}")
#
#         with open(json_path, "w") as fp:
#             json.dump(
#                 obj=self.Schema(exclude=("json_path",)).dump(
#                     self,
#                 ),
#                 fp=fp,
#                 indent=2,
#             )
#
#     # @classmethod
#     # def init_kwargs(cls) -> T.List[str]:
#     #     return inspect.getfullargspec(cls.__init__).args[1:]
