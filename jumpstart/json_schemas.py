#!/usr/bin/env python3

# from __future__ import annotations

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
@dataclass(order=True)
class AptTemplateParams:
    """JSON Parameters required to fill in the Apt templates"""

    pkgs: T.List[str] = field(default_factory=list)
    ppas: T.List[str] = field(default_factory=list)
    Schema: T.ClassVar[T.Type[ma.Schema]] = ma.Schema


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
@dataclass(order=True)
class SnapTemplateParams:
    """JSON Parameters required to fill in the Snap templates"""

    pkg: str = field(default="")
    policy: SnapPolicy = field(default="")
    Schema: T.ClassVar[T.Type[ma.Schema]] = ma.Schema


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
            # TODO SHell escape as well!
            self.url = self.static_url


@add_schema
@dataclass(order=True)
class DebTemplateParams:
    """JSON Parameters required to fill in the Deb templates"""

    src: DownloadSource
    Schema: T.ClassVar[T.Type[ma.Schema]] = ma.Schema


@add_schema
@dataclass(order=True)
class TemplateParams:
    apt: T.Optional[AptTemplateParams] = None
    snap: T.Optional[SnapTemplateParams] = None
    deb: T.Optional[DebTemplateParams] = None
    Schema: T.ClassVar[T.Type[ma.Schema]] = ma.Schema


@add_schema
@dataclass(order=True)
class Metadata:
    """For each Metadta JSON file, what can we expect to find"""

    json_path: Path
    name: str
    template_params: TemplateParams = dataclasses.field(repr=False, default_factory=TemplateParams)
    url: str = dataclasses.field(repr=False, default="")
    tags: T.List[str] = dataclasses.field(repr=False, default_factory=list)
    preference: T.List[str] = dataclasses.field(repr=False, default_factory=list)
    Schema: T.ClassVar[T.Type[ma.Schema]] = ma.Schema

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
    #
    # @classmethod
    # def from_json(cls, p: pathlib.Path) -> 'Metadata':
    #
    #     assert p.is_file()
    #     assert p.suffix.lower() == '.json'
    #
    #     if not p.stat().st_size:
    #         return cls()
    #
    #     with safe_open(p) as fp:
    #         d = json.load(fp)
    #         return cls(**{k: v for k, v in d.items() if k in cls.init_kwargs()})
    #
    # def fill_with_defaults(self, p: pathlib.Path) -> None:
    #     if p.is_file():
    #         p = p.parent
    #     self.name = self.name or p.name
    #     self.url = self.url or f"https://www.google.com/search?q={html.escape(self.name)}"
    #     self.tags = self.tags or []
    #     self.preference = self.preference or []
    #
    # def to_json(self, p: pathlib.Path) -> None:
    #     with safe_open(p, "w") as fp:
    #         json.dump(obj={k: getattr(self, k) for k in self.init_kwargs()}, fp=fp, indent=4)
