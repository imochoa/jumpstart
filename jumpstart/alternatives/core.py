#!/usr/bin/env python3

from __future__ import annotations

# stdlib imports
from abc import ABC, abstractmethod
import codecs
from collections import abc
from dataclasses import dataclass
import enum
import functools
import inspect
import json
import logging
import os
import pathlib
import subprocess
import typing as T

# 1st party imports
from jumpstart.cli_utils import bcolors, colorize, debug, info
from jumpstart.utils import load_script, safe_open

logger = logging.getLogger(__name__)


auto_comment_re = r"^#\s*>+\s*(?P<section>\S+)(?P<data>.*)$"


class InvalidDirname(ValueError):
    pass


class AbstractAlternative(ABC):
    dirname = ""

    def __init__(
        self,
        install_script: pathlib.Path,
        setup_script: pathlib.Path,
        update_script: pathlib.Path,
        remove_script: pathlib.Path,
        status_script: pathlib.Path,
        version_script: pathlib.Path,
    ):
        self.install_script = install_script
        self.setup_script = setup_script
        self.update_script = update_script
        self.remove_script = remove_script
        self.status_script = status_script
        self.version_script = version_script

        super().__init__()

    @classmethod
    def template(cls) -> None:
        info(f"[TODO] {cls}!")

    @functools.lru_cache(maxsize=None)
    def is_installed(self) -> T.Optional[bool]:
        """
        True-> Installed
        False -> Not Installed
        None -> Could not check
        """
        if not self.status_script.is_file():
            return None

        p = subprocess.run(
            f". {self.status_script} && echo $missing",
            capture_output=True,
            shell=True,
        )

        if p.returncode != 0:
            return None
        try:
            return int(p.stdout.split()[-1]) == 0
        except Exception:
            return None

    def generate_std_files(self) -> bool:
        logger.info(f"No std file handler for {self}")
        return False

    @property
    def auto_shebang(self) -> str:
        return r"#!/usr/bin/env sh" "\n# DO NOT MODIFY!" "\n# THIS FILE WAS AUTOGENERATED" "\n"

    @classmethod
    def from_dir(cls, dir: pathlib.Path) -> T.List[AbstractAlternative]:

        alt_dirs = [d for d in dir.iterdir() if d.is_dir()]

        alt_dict: T.Dict[T.Type[AbstractAlternative], T.List[AbstractAlternative]] = dict()
        for subcls in cls.__subclasses__():
            for alt_dir in alt_dirs:
                try:
                    obj = subcls.from_alt_dir(alt_dir)
                    alt_dict.setdefault(subcls, []).append(obj)
                except InvalidDirname:
                    pass
        # TODO check max one in each key

        return [vs[0] for vs in alt_dict.values()]

    @classmethod
    def from_alt_dir(cls, dir: pathlib.Path) -> AbstractAlternative:
        if not dir.name.lower() == cls.dirname.lower():
            raise InvalidDirname(f"Cannot be {cls} since {dir.name} != {cls.dirname}")

        return cls(
            install_script=dir / "install.sh",
            setup_script=dir / "setup.sh",
            remove_script=dir / "remove.sh",
            update_script=dir / "update.sh",
            status_script=dir / "status.sh",
            version_script=dir / "version.sh",
        )