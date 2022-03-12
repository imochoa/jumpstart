#!/usr/bin/env python3

# from __future__ import annotations

# stdlib imports
from dataclasses import dataclass, field
import functools
import pathlib
import platform
import subprocess
from types import SimpleNamespace
import typing as T

# 3rd party imports
import jinja2
from loguru import logger

# 1st party imports
from jumpstart.constants import (
    KNOWN_TEMPLATES,
    Filename,
    Filenames,
    Paths,
    template_env,
    template_loader,
)
from jumpstart.json_schemas import AptTemplateParams, Metadata, SnapTemplateParams

Architecture = T.NewType("Architecture", str)


class Architectures(SimpleNamespace):
    """What CPU chipset is being used"""

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

    unknown: Platform = Platform("unknown")
    linux: Platform = Platform("linux")
    mac: Platform = Platform("mac")

    @staticmethod
    def from_runtime() -> Platform:
        return Platform(platform.system())


OS = T.NewType("OS", str)


class OSs(SimpleNamespace):
    """What exact Operating System (OS) are we dealing with"""

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


@dataclass
class SystemContext:
    """Combination of Architecture, Platform and OS"""

    architecture: Architecture
    platform: Platform
    os: OS

    @staticmethod
    @functools.lru_cache()
    def from_runtime() -> "SystemContext":
        return SystemContext(
            architecture=Architectures.from_runtime(),
            platform=Platforms.from_runtime(),
            os=OSs.from_runtime(),
        )


@dataclass
class Alternative:
    """"""

    templates: T.Dict[Filename, jinja2.Template]
    out_dir: pathlib.Path
    params: T.Union[SnapTemplateParams, AptTemplateParams]

    def render_templates(self) -> T.Dict["Filename", pathlib.Path]:
        output_map = dict()
        for filename, template in self.templates.items():
            output_path = self.out_dir / filename
            output_map[filename] = output_path
            with open(output_path, "w") as fp:
                fp.write(template.render(self.params.__dict__))
        return output_map


@dataclass
class Component:
    """Combination of an installable component plus its metdata and required scripts"""

    metadata: Metadata
    root_dir: pathlib.Path
    alternatives: T.List["Alternative"] = field(default_factory=list)

    # script_map: T.Dict[Filename, pathlib.Path]
    # template_map: T.Dict[Filename, pathlib.Path]

    # @functools.lru_cache(maxsize=None)
    # def is_installed(self) -> T.Optional[bool]:
    #     """
    #     True-> Installed
    #     False -> Not Installed
    #     None -> Could not check
    #     """
    #     if not self.status_script.is_file():
    #         return None
    #
    #     p = subprocess.run(
    #         f". {self.status_script} && echo $missing",
    #         capture_output=True,
    #         shell=True,
    #     )
    #
    #     if p.returncode != 0:
    #         return None
    #     try:
    #         return int(p.stdout.split()[-1]) == 0
    #     except Exception:
    #         return None

    @classmethod
    def from_path(cls: T.Type["Component"], p: pathlib.Path) -> "Component":

        metadata = Metadata.from_path(p)
        root_dir = metadata.json_path.parent  # type: ignore [attr-defined]

        alternatives: T.List["Alternative"] = []
        t_cls: "Alternative"
        for json_name, params in metadata.template_params.__dict__.items():
            if not params:
                continue
            # t_cls = next(cls for cls in Alternative.__subclasses__() if t_name in cls.__name__.lower())
            # alternatives.append(t_cls(template_dir=t_path, out_dir=root_dir / t_name, **params))

            alternatives.append(
                Alternative(
                    templates=KNOWN_TEMPLATES[Filename(json_name)],
                    out_dir=root_dir / json_name,
                    params=params,
                )
            )

        return cls(
            metadata=metadata,
            root_dir=root_dir,
            alternatives=alternatives,
        )

    def render_templates(self: T.Any) -> None:
        for alt in self.alternatives:
            alt.render_templates()

        # return cls(name=name, script_map=script2path, template_map=template2path)

    # @classmethod
    # def from_alt_dir(cls, dir: pathlib.Path) -> AbstractAlternative:
    #     if not dir.name.lower() == cls.dirname.lower():
    #         raise InvalidDirname(f"Cannot be {cls} since {dir.name} != {cls.dirname}")
    #
    #     return cls(
    #         install_script=dir / "install.sh",
    #         setup_script=dir / "setup.sh",
    #         remove_script=dir / "remove.sh",
    #         update_script=dir / "update.sh",
    #         status_script=dir / "status.sh",
    #         version_script=dir / "version.sh",
    #     )
