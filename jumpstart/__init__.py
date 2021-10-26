#!/usr/bin/env python3

from __future__ import annotations

# stdlib imports
from abc import ABC, abstractmethod
import codecs
from collections import abc
from dataclasses import dataclass
import enum
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

METADATA_JSON = dict(
    name=str,
    url=str,
    tags=T.List[str],
    preference=T.List[str],
)


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
            raise FileNotFoundError(f"{path} was missing!")
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
        except FileNotFoundError:
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
