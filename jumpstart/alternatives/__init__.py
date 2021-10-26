#!/usr/bin/env python3

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
from jumpstart.alternatives.apt import AptAlternative
from jumpstart.alternatives.bin import BinAlternative
from jumpstart.alternatives.core import AbstractAlternative
from jumpstart.alternatives.deb import DebAlternative
from jumpstart.alternatives.snap import SnapAlternative
from jumpstart.alternatives.src import SrcAlternative

# CLS_MAPPING: T.Dict[str, AbstractAlternative] = {cls.install_type.lower(): cls for cls in AbstractAlternative.__subclasses__()}
#
#
# @staticmethod
# def _from_dir(dir: os.PathLike) -> T.Optional[AbstractAlternative]:
#     dir_p: pathlib.Path = pathlib.Path(dir)
#     name: str = dir_p.name.lower()
#
#     if not dir_p.is_dir() or name not in CLS_MAPPING:
#         return None
#
#     child_cls = CLS_MAPPING[name]
#
#     contents = list(dir_p.iterdir())
#     install_script = next((p for p in contents if p.stem.lower() == "install"), None)
#     # remove_script = next((p for p in contents if p.stem.lower() == "remove"), None)
#     # status_script = next((p for p in contents if p.stem.lower() == "status"), None)
#     # other_script = next((p for p in contents if p.stem.lower() == "hooho"), None)
#
#     return child_cls(
#         name=dir_p.parent,
#         install_script=install_script,
#     )
#
#     # if dir_p.is_dir() and dir_p.name.lower() in CLS_MAPPING:
#     #     child_cls = CLS_MAPPING[p.name.lower()]
#     #     install_script_path = p / 'install'
#     #     return child_cls(install_script_path)
#
#
# AbstractAlternative.from_dir = _from_dir
#
# o = AbstractAlternative.from_dir("/home/imochoa/Code/jumpstart/index/arandr/apt")
#
# print(o)
#
# o = AbstractAlternative.from_dir("/home/imochoa/Code/jumpstart/index/arduino-ide/snap")
#
# print(o)
