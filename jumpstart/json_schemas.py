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

#
# Architecture = T.NewType("Arch", str)
#
#
# class Architectures(SimpleNamespace):
#     """What CPU chipset is being used"""
#     unknown = Architecture("unknown")
#     x64 = Architecture("x64")
#     arm = Architecture("arm")
#
#     @staticmethod
#     def from_runtime() -> Architecture:
#         arch = Architectures.unknown
#         if platform.machine().endswith("64"):
#             arch = Architectures.x64
#         return arch
#
#
# Platform = T.NewType("Platform", str)
#
#
# class Platforms(SimpleNamespace):
#     """What framework are we dealing with"""
#     unknown: Platform = Platform("unknown")
#     linux: Platform = Platform("linux")
#     mac: Platform = Platform("mac")
#
#     @staticmethod
#     def from_runtime() -> Platform:
#         return Platform(platform.system())
#
#
# OS = T.NewType("OS", str)
#
#
# class OSs(SimpleNamespace):
#     """What exact Operating System (OS) are we dealing with"""
#     unknown = OS("unknown")
#     ubuntu2004 = OS("ubuntu2004")
#
#     @staticmethod
#     def from_runtime():
#         os = OSs.unknown
#         if Platforms.from_runtime() == Platforms.linux:
#             p_stdout = subprocess.check_output(["lsb_release", "-a"])
#             if p_stdout:
#                 os = OS(p_stdout.decode("utf8").split("\n")[1].split(":")[1].strip())
#         return os
#
#
# Filename = T.NewType("Filename", str)
#
#
# class Filenames(SimpleNamespace):
#     """
#     Accepted filenames for each installable. The extensions are usually ".sh"
#     """
#     install: Filename = Filename('install')
#     setup: Filename = Filename('setup')
#     update: Filename = Filename('update')
#     remove: Filename = Filename('remove')
#     status: Filename = Filename('status')
#     version: Filename = Filename('version')
#     metadata: Filename = Filename('metadata')
#
#     @classmethod
#     @functools.lru_cache()
#     def as_set(cls) -> T.Set['Filenames']:
#         return {s for s in cls.__dict__.keys() if not s.startswith('__')}


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

#
# @dataclass
# class SystemContext:
#     """Combination of Architecture, Platform and OS"""
#     architecture: Architecture
#     platform: Platform
#     os: OS
#
#     @staticmethod
#     @functools.lru_cache()
#     def from_runtime() -> 'SystemContext':
#         return SystemContext(
#             architecture=Architectures.from_runtime(),
#             platform=Platforms.from_runtime(),
#             os=OSs.from_runtime(),
#         )


@add_schema
@dataclass(order=True)
class AptTemplateParams:
    """JSON Parameters required to fill in the Apt templates"""

    pkgs: T.List[str] = field(default_factory=list)
    ppas: T.List[str] = field(default_factory=list)


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


#
# @add_schema
# @dataclass(order=True)
# class DownloadSource:
#     """JSON Parameters required to fill in the Snap templates"""
#
#     url: str = field(default="")
#     github_url: str = field(default="")


# @add_schema
# @dataclass(order=True)
# class DebTemplateParams:
#     """JSON Parameters required to fill in the Deb templates"""
#     pkg:str = field(default='')
#     policy: str = field(default='')


@add_schema
@dataclass(order=True)
class TemplateParams:
    apt: T.Optional[AptTemplateParams] = None
    snap: T.Optional[SnapTemplateParams] = None
    # deb:DebTemplateParams


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


# b = Metadata.from_path(pathlib.Path('/home/imochoa/Code/jumpstart/index/x64__ubuntu2004/7zip/'))
#
#
# @dataclass
# class Alternative:
#     """"""
#     templates: T.Dict[Filename, jinja2.Template]
#     out_dir: pathlib.Path
#     params: T.Union[SnapTemplateParams, AptTemplateParams]
#
#     def render_templates(self) -> T.Dict:
#         output_map = dict()
#         for filename, template in self.templates.items():
#             output_path = self.out_dir / filename
#             output_map[filename] = output_path
#             with open(output_path, 'w') as fp:
#                 fp.write(template.render(self.params.__dict__))
#         return output_map
#
#
# @dataclass
# class Component:
#     """Combination of an installable component plus its metdata and required scripts"""
#     metadata: Metadata
#     root_dir: pathlib.Path
#     alternatives: T.List['Alternative'] = field(default_factory=list)
#
#     # script_map: T.Dict[Filename, pathlib.Path]
#     # template_map: T.Dict[Filename, pathlib.Path]
#
#     @functools.lru_cache(maxsize=None)
#     def is_installed(self) -> T.Optional[bool]:
#         """
#         True-> Installed
#         False -> Not Installed
#         None -> Could not check
#         """
#         if not self.status_script.is_file():
#             return None
#
#         p = subprocess.run(
#             f". {self.status_script} && echo $missing",
#             capture_output=True,
#             shell=True,
#         )
#
#         if p.returncode != 0:
#             return None
#         try:
#             return int(p.stdout.split()[-1]) == 0
#         except Exception:
#             return None
#
#     @classmethod
#     def from_path(cls: T.Any, p: pathlib.Path) -> 'Component':
#
#         metadata = Metadata.from_path(p)
#         root_dir = metadata.json_path.parent
#
#         alternatives: T.List['Alternative'] = []
#         t_cls: 'Alternative'
#         for json_name, params in metadata.template_params.__dict__.items():
#             if not params:
#                 continue
#             # t_cls = next(cls for cls in Alternative.__subclasses__() if t_name in cls.__name__.lower())
#             # alternatives.append(t_cls(template_dir=t_path, out_dir=root_dir / t_name, **params))
#
#             alternatives.append(Alternative(templates=KNOWN_TEMPLATES[json_name],
#                                             out_dir=root_dir / json_name,
#                                             params=params,
#                                             )
#                                 )
#
#         return cls(
#             metadata=metadata,
#             root_dir=root_dir,
#             alternatives=alternatives,
#         )
#
#     def render_templates(self):
#         for alt in self.alternatives:
#             alt.render_templates()
#
#         # return cls(name=name, script_map=script2path, template_map=template2path)
#
#     # @classmethod
#     # def from_alt_dir(cls, dir: pathlib.Path) -> AbstractAlternative:
#     #     if not dir.name.lower() == cls.dirname.lower():
#     #         raise InvalidDirname(f"Cannot be {cls} since {dir.name} != {cls.dirname}")
#     #
#     #     return cls(
#     #         install_script=dir / "install.sh",
#     #         setup_script=dir / "setup.sh",
#     #         remove_script=dir / "remove.sh",
#     #         update_script=dir / "update.sh",
#     #         status_script=dir / "status.sh",
#     #         version_script=dir / "version.sh",
#     #     )
#
# # c = Component.from_path(pathlib.Path('/home/imochoa/Code/jumpstart/index/x64__ubuntu2004/7zip/'))
# # c.render_templates()
# # a = Method.from_dir(pathlib.Path('/home/imochoa/Code/jumpstart/index/x64__ubuntu2004/7zip/apt'))
#
# # KNOWN_ALTERNATIVES: T.List[Alternative] = []
#
# # @dataclass
# # class Alternative:
# #     path: pathlib.Path
# #     metadata: Metadata
# #     methods: T.List[Method]
# #     sys_context: T.ClassVar[SystemContext] = SystemContext.from_runtime()
# #
# #     @property
# #     def metadata_json(self) -> pathlib.Path:
# #         path = self.path / "metadata.json"
# #         if not path.is_file():
# #             logger.error(f"{path} was missing!")
# #         return path
#
# # def refresh(self):
# #     # Check JSON file
# #     json_path = self.path / "metadata.json"
# #     metadata = dict()
# #     if not json_path.is_file():
# #         logger.warning(f"{json_path} was missing!")
# #         # raise FileNotFoundError(f"{json_path} was missing!")
# #     else:
# #         # with codecs.open(json_path, "r", encoding="utf-8", errors="ignore") as fp:
# #         #     metadata = json.load(fp)
# #         with safe_open(json_path) as fp:
# #             metadata = json.load(fp)
# #
# #     # keys missing?
# #
# #     # types
# #
# #     # format!
# #
# #     # children
# #     for obj in self.alternatives:
# #         obj.refresh()
#
# # @classmethod
# # def from_dir(
# #         cls,
# #         dirpath: pathlib.Path,
# #         sys_context: T.Optional[SystemContext] = None,
# # ) -> Installable:
# #
# #     curr_context: SystemContext
# #     if sys_context is None:
# #         curr_context = cls.sys_context
# #     else:
# #         curr_context = sys_context
# #
# #     # Read the file
# #     json_path = dirpath / "metadata.json"
# #     try:
# #         with safe_open(json_path) as fp:
# #             metadata = json.load(fp)
# #     except (FileNotFoundError, json.JSONDecodeError):
# #         logger.error(f"No {json_path} found...")
# #         metadata = dict()
# #
# #     name = metadata.get("name", f"MISSING KEY 'name' in [{json_path}]")
# #     url = metadata.get("url", f"MISSING KEY 'url' in [{json_path}]")
# #     tags = metadata.get("tags", [f"MISSING KEY 'tags' in [{json_path}]"])
# #     preference = metadata.get("preference", [])
# #
# #     alts = AbstractAlternative.from_dir(dirpath)
# #     altname_map = {a.dirname.lower(): a for a in alts}
# #     preference = [p.lower() for p in preference]
# #     others = sorted(k for k in altname_map.keys() if k not in preference)
# #     sorted_alternatives = [altname_map[p] for p in preference + others if p in altname_map]
# #
# #     return Installable(
# #         path=dirpath,
# #         name=name,
# #         url=url,
# #         tags=tags,
# #         alternatives=sorted_alternatives,
# #         context=context,
# #     )
# #
# # b = Installable.from_dir(pathlib.Path('/home/imochoa/Code/jumpstart/index/x64__ubuntu2004/7zip/'))
# # class AbstractAlternative(ABC):
# #     dirname = ""
# #
# #     def __init__(
# #         self,
# #         install_script: pathlib.Path,
# #         setup_script: pathlib.Path,
# #         update_script: pathlib.Path,
# #         remove_script: pathlib.Path,
# #         status_script: pathlib.Path,
# #         version_script: pathlib.Path,
# #     ):
# #         self.install_script = install_script
# #         self.setup_script = setup_script
# #         self.update_script = update_script
# #         self.remove_script = remove_script
# #         self.status_script = status_script
# #         self.version_script = version_script
# #
# #         super().__init__()
# #
# #     @classmethod
# #     def template(cls) -> None:
# #         info(f"[TODO] {cls}!")
# #
# #     @functools.lru_cache(maxsize=None)
# #     def is_installed(self) -> T.Optional[bool]:
# #         """
# #         True-> Installed
# #         False -> Not Installed
# #         None -> Could not check
# #         """
# #         if not self.status_script.is_file():
# #             return None
# #
# #         p = subprocess.run(
# #             f". {self.status_script} && echo $missing",
# #             capture_output=True,
# #             shell=True,
# #         )
# #
# #         if p.returncode != 0:
# #             return None
# #         try:
# #             return int(p.stdout.split()[-1]) == 0
# #         except Exception:
# #             return None
# #
# #     def generate_std_files(self) -> bool:
# #         logger.info(f"No std file handler for {self}")
# #         return False
# #
# #     @property
# #     def auto_shebang(self) -> str:
# #         return r"#!/usr/bin/env sh" "\n# DO NOT MODIFY!" "\n# THIS FILE WAS AUTOGENERATED" "\n"
# #
# #     @classmethod
# #     def from_dir(cls, dir: pathlib.Path) -> T.List[AbstractAlternative]:
# #
# #         alt_dirs = [d for d in dir.iterdir() if d.is_dir()]
# #
# #         alt_dict: T.Dict[T.Type[AbstractAlternative], T.List[AbstractAlternative]] = dict()
# #         for subcls in cls.__subclasses__():
# #             for alt_dir in alt_dirs:
# #                 try:
# #                     obj = subcls.from_alt_dir(alt_dir)
# #                     alt_dict.setdefault(subcls, []).append(obj)
# #                 except InvalidDirname:
# #                     pass
# #         # TODO check max one in each key
# #
# #         return [vs[0] for vs in alt_dict.values()]
# #
# #     @classmethod
# #     def from_alt_dir(cls, dir: pathlib.Path) -> AbstractAlternative:
# #         if not dir.name.lower() == cls.dirname.lower():
# #             raise InvalidDirname(f"Cannot be {cls} since {dir.name} != {cls.dirname}")
# #
# #         return cls(
# #             install_script=dir / "install.sh",
# #             setup_script=dir / "setup.sh",
# #             remove_script=dir / "remove.sh",
# #             update_script=dir / "update.sh",
# #             status_script=dir / "status.sh",
# #             version_script=dir / "version.sh",
# #         )
