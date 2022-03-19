#!/usr/bin/env python3

# stdlib imports
from dataclasses import dataclass, field
import functools
import platform
import subprocess
from types import SimpleNamespace
import typing as T

# 3rd party imports
from loguru import logger
import marshmallow as ma
from marshmallow_dataclass import NewType, add_schema

Architecture = T.NewType("Architecture", str)


class Architectures(SimpleNamespace):
    """What CPU chipset is being used"""

    any = Architecture("any")
    unknown = Architecture("unknown")
    x64 = Architecture("x64")
    arm = Architecture("arm")

    @staticmethod
    def from_runtime() -> Architecture:
        arch = Architectures.unknown
        if platform.machine().endswith("64"):
            arch = Architectures.x64
        return arch


Platform = T.NewType("Platform", str)


class Platforms(SimpleNamespace):
    """What framework are we dealing with"""

    any = Platform("any")
    unknown: Platform = Platform("unknown")
    linux: Platform = Platform("linux")
    mac: Platform = Platform("mac")

    @staticmethod
    def from_runtime() -> Platform:
        return Platform(platform.system())


OS = T.NewType("OS", str)


class OSs(SimpleNamespace):
    """What exact Operating System (OS) are we dealing with"""

    any = OS("any")
    unknown = OS("unknown")
    ubuntu2004 = OS("ubuntu2004")

    @staticmethod
    def from_runtime() -> "OS":
        os_var = OSs.unknown
        if Platforms.from_runtime() == Platforms.linux:
            p_stdout = subprocess.check_output(["lsb_release", "-a"])
            if p_stdout:
                os_var = OS(p_stdout.decode("utf8").split("\n")[1].split(":")[1].strip())
        return os_var


@add_schema
@dataclass(order=True, frozen=True)
class SystemContext:
    """Combination of Architecture, Platform and OS"""

    platform: Platform = Platforms.any
    os: OS = OSs.any
    architecture: Architecture = Architectures.any

    class Meta:
        ordered = True

    @ma.post_dump
    def remove_skip_values(self: "SystemContext", data: T.Dict[str, T.Any], **kwargs: T.Any) -> T.Dict[str, T.Any]:
        """Ignore empty/any fields"""
        return {
            key: value for key, value in data.items() if value not in {None, OSs.any, Architectures.any, Platforms.any}
        }

    @staticmethod
    @functools.lru_cache()
    def from_runtime() -> "SystemContext":
        return SystemContext(
            architecture=Architectures.from_runtime(),
            platform=Platforms.from_runtime(),
            os=OSs.from_runtime(),
        )

    @staticmethod
    def any() -> "SystemContext":
        return SystemContext(
            # platform=Platforms.any,
            platform=Platforms.linux,
            os=OSs.any,
            architecture=Architectures.any,
        )
