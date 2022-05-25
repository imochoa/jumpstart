#!/usr/bin/env python3

# stdlib imports
import codecs
from dataclasses import dataclass, field
import pathlib
import typing as T

# 3rd party imports
from loguru import logger
import marshmallow as ma
from marshmallow.validate import OneOf
from marshmallow_dataclass import NewType, add_schema

# 1st party imports
from jumpstart.constants import Paths, template_env, template_loader


def render(pkg, basepath: pathlib.Path) -> None:
    """
    basepath: top-level pkg dir
    """
    this_name = type(pkg).__name__
    this_templates_dir = Paths.TEMPLATE_DIR / this_name.lower()

    if not this_templates_dir.is_dir():
        raise OSError(f"Missing template dir {this_templates_dir}")

    template_paths = (f for f in this_templates_dir.iterdir() if f.suffix.lower() == ".j2")

    for t_path in template_paths:
        j2_relpath = t_path.relative_to(Paths.TEMPLATE_DIR)
        template = template_env.get_template(str(j2_relpath))
        dest_path = basepath / j2_relpath.parent / j2_relpath.stem
        with codecs.open(str(dest_path), "w", encoding="utf-8", errors="ignore") as fp:
            fp.write(template.render(pkg.Schema().dump(pkg)))
        # logger.info(f"Wrote {dest_path}")
        logger.info(f"\t{dest_path.relative_to(basepath)}")


@add_schema
@dataclass
class Apt:
    """JSON Parameters required to fill in the Apt templates"""

    pkgs: T.List[str]
    ppas: T.List[str] = field(default_factory=list)
    priority: int = 100
    Schema: T.ClassVar[T.Type[ma.Schema]] = ma.Schema

    class Meta:
        ordered = True

    def update(self) -> None:
        pass

    # @ma.post_dump
    # def remove_skip_values(self: "AltParams",
    #                        data: T.Dict[str, T.Any],
    #                        **kwargs: T.Any,
    #                        ) -> T.Dict[str, T.Any]:
    #     """Ignore empty fields"""
    #     return {key: value for key, value in data.items() if value is not None}


SnapPolicy = NewType("SnapPolicy", str, validate=OneOf({"", "edge", "classic"}))


@add_schema
@dataclass
class Snap:
    pkg: str
    policy: SnapPolicy = ""
    priority: int = 100
    Schema: T.ClassVar[T.Type[ma.Schema]] = ma.Schema

    class Meta:
        ordered = True

    def update(self) -> None:
        pass


@add_schema
@dataclass
class Deb:
    priority: int = 100
    Schema: T.ClassVar[T.Type[ma.Schema]] = ma.Schema

    class Meta:
        ordered = True

    def update(self) -> None:
        pass


@add_schema
@dataclass
class AppImage:
    priority: int = 100
    Schema: T.ClassVar[T.Type[ma.Schema]] = ma.Schema

    class Meta:
        ordered = True

    def update(self) -> None:
        pass


@add_schema
@dataclass
class Bin:
    priority: int = 100
    Schema: T.ClassVar[T.Type[ma.Schema]] = ma.Schema

    class Meta:
        ordered = True

    def update(self) -> None:
        pass


@add_schema
@dataclass
class PipX:
    priority: int = 100
    Schema: T.ClassVar[T.Type[ma.Schema]] = ma.Schema

    class Meta:
        ordered = True

    def update(self) -> None:
        pass


@add_schema
@dataclass
class Src:
    priority: int = 100
    Schema: T.ClassVar[T.Type[ma.Schema]] = ma.Schema

    class Meta:
        ordered = True

    def update(self) -> None:
        pass
