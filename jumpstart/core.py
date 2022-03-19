#!/usr/bin/env python3

# from __future__ import annotations

# stdlib imports
from dataclasses import dataclass, field
import pathlib
import typing as T

# 3rd party imports
import jinja2
from loguru import logger

# 1st party imports
from jumpstart.constants import (
    KNOWN_TEMPLATES,
    Filename,
)
from jumpstart.metadata_schema import Metadata
from jumpstart.metadata_schema.sys_context import SystemContext

if T.TYPE_CHECKING:
    # 1st party imports
    # from jumpstart.metadata_schema.sys_context import
    from jumpstart.metadata_schema.templates import (
        AptTemplateParams,
        SnapTemplateParams,
    )


@dataclass
class Alternative:
    """"""

    templates: T.Dict[Filename, jinja2.Template]
    out_dir: pathlib.Path
    system_context: SystemContext
    params: T.Union["SnapTemplateParams", "AptTemplateParams"]

    def render_templates(self, mkdir: bool = True) -> T.Dict["Filename", pathlib.Path]:
        if not self.out_dir.is_dir() and mkdir:
            self.out_dir.mkdir(parents=True, exist_ok=True)
        output_map = dict()
        for filename, template in self.templates.items():
            output_path = self.out_dir / filename
            output_map[filename] = output_path
            with open(output_path, "w") as fp:
                fp.write(template.render(self.params.__dict__))
        return output_map

    # def __hash__(self):
    #     pass


@dataclass
class Component:
    """Combination of an installable component plus its metadata and required scripts"""

    metadata: Metadata
    root_dir: pathlib.Path
    alternatives: T.List["Alternative"] = field(default_factory=list)


    @classmethod
    def from_path(cls: T.Type["Component"], p: pathlib.Path) -> "Component":

        metadata = Metadata.from_path(p)
        root_dir = metadata.json_path.parent  # type: ignore [attr-defined]

        alternatives: T.List["Alternative"] = []
        t_cls: "Alternative"

        for params_obj in metadata.alt_params:

            params_dict = params_obj.__dict__
            system_context = params_dict.pop("system_context")

            for alt_name, params in params_dict.items():
                if not params:
                    continue

                # Any alternatives with these keys will receive them from "metadata.json" unless they overwrite it
                DEFAULT_MAP = dict(name=metadata.name)
                for k,v in DEFAULT_MAP.items():
                    try:
                        if not getattr(params,k):
                            setattr(params,k,v)
                    except AttributeError:
                        continue


                alternatives.append(
                    Alternative(
                        templates=KNOWN_TEMPLATES[Filename(alt_name)],
                        out_dir=root_dir / alt_name,
                        system_context=system_context,
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
