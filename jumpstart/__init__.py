#!/usr/bin/env python3

from __future__ import annotations

# stdlib imports
from abc import ABC, abstractmethod
import codecs
from collections import abc
import dataclasses
from dataclasses import dataclass
import enum
import html
import inspect
import json
import logging
import os
import pathlib
import typing as T

# 1st party imports
from jumpstart.alternatives import AbstractAlternative
from jumpstart.constants import Architecture, OperatingSystem
from jumpstart.utils import safe_open

logger = logging.getLogger(__name__)


@dataclass
class Installable:
    path: pathlib.Path
    name: str
    url: str
    tags: T.List[str]
    alternatives: T.List[AbstractAlternative]
    architecture: Architecture = Architecture.unknown
    operating_system: OperatingSystem = OperatingSystem.unknown

    @property
    def metadata_json(self) -> pathlib.Path:
        path = self.path / "metadata.json"
        if not path.is_file():
            logger.error(f"{path} was missing!")
            # raise FileNotFoundError(f"{path} was missing!")
        return path

    # def refresh(self):
    #     # Check JSON file
    #     json_path = self.path / "metadata.json"
    #     metadata = dict()
    #     if not json_path.is_file():
    #         logger.warning(f"{json_path} was missing!")
    #         # raise FileNotFoundError(f"{json_path} was missing!")
    #     else:
    #         # with codecs.open(json_path, "r", encoding="utf-8", errors="ignore") as fp:
    #         #     metadata = json.load(fp)
    #         with safe_open(json_path) as fp:
    #             metadata = json.load(fp)
    #
    #     # keys missing?
    #
    #     # types
    #
    #     # format!
    #
    #     # children
    #     for obj in self.alternatives:
    #         obj.refresh()

    @classmethod
    def from_dir(
        cls,
        dirpath: pathlib.Path,
        architecture: Architecture = Architecture.unknown,
        operating_system: OperatingSystem = OperatingSystem.unknown,
    ) -> Installable:

        # Read the file
        json_path = dirpath / "metadata.json"
        try:
            with safe_open(json_path) as fp:
                metadata = json.load(fp)
        except (FileNotFoundError, json.JSONDecodeError):
            logging.error(f"No {json_path} found...")
            metadata = dict()

        name = metadata.get("name", f"MISSING KEY 'name' in [{json_path}]")
        url = metadata.get("url", f"MISSING KEY 'url' in [{json_path}]")
        tags = metadata.get("tags", [f"MISSING KEY 'tags' in [{json_path}]"])
        preference = metadata.get("preference", [])

        alts = AbstractAlternative.from_dir(dirpath)
        altname_map = {a.dirname.lower(): a for a in alts}
        preference = [p.lower() for p in preference]
        others = sorted(k for k in altname_map.keys() if k not in preference)
        sorted_alternatives = [altname_map[p] for p in preference + others if p in altname_map]

        return Installable(
            path=dirpath,
            name=name,
            url=url,
            tags=tags,
            alternatives=sorted_alternatives,
            architecture=architecture,
            operating_system=operating_system,
        )


@dataclass
class Metadata:
    name: str = dataclasses.field(default="")
    url: str = dataclasses.field(default="")
    tags: T.List[str] = dataclasses.field(default_factory=list)
    preference: T.List[str] = dataclasses.field(default_factory=list)

    @classmethod
    def init_kwargs(cls) -> T.List[str]:
        return inspect.getfullargspec(cls.__init__).args[1:]

    @classmethod
    def from_json(cls, p: pathlib.Path) -> Metadata:
        if not p.stat().st_size:
            return cls()

        with safe_open(p) as fp:
            d = json.load(fp)
            return cls(**{k: v for k, v in d.items() if k in cls.init_kwargs()})

    def fill_with_defaults(self, p: pathlib.Path) -> None:
        if p.is_file():
            p = p.parent
        self.name = self.name or p.name
        self.url = self.url or f"https://www.google.com/search?q={html.escape(self.name)}"
        self.tags = self.tags or []
        self.preference = self.preference or []

    def to_json(self, p: pathlib.Path) -> None:
        with safe_open(p, "w") as fp:
            json.dump(obj={k: getattr(self, k) for k in self.init_kwargs()}, fp=fp, indent=4)


# METADATA_JSON = dict(
#     name=str,
#     url=str,
#     tags=T.List[str],
#     preference=T.List[str],
# )

# def load_metadata_json(json_path: pathlib.Path) -> T.Dict[str, str]:
#     print("do!")


# AbstractProgram.from_dir('/home/imochoa/Code/jumpstart/index/arandr')


# # Important filenames
# class Scripts(enum.Enum):
#     install = "install"
#     remove = "remove"
#     update = "update"
#     status = "status"
#
#
# class Alternatives(enum.Enum):
#     apt = "apt"
#     snap = "snap"
#     src = "src"
#     bin = "bin"
#
#
# # Important filenames
# class AppFilenames(enum.Enum):
#     install = "install"
#     remove = "remove"
#     update = "update"
#     status = "status"
