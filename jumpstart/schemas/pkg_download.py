#!/usr/bin/env python3
# stdlib imports
from dataclasses import dataclass, field
import pathlib
from shlex import quote as sh_quote
import subprocess
import typing as T
from urllib.parse import quote as url_quote

# 3rd party imports
from loguru import logger
import marshmallow as ma
from marshmallow_dataclass import NewType, add_schema
from marshmallow_polyfield import PolyFieldBase

# 1st party imports
from jumpstart.constants import ARCHIVE_EXTS


def is_shell_cmd(cmd: str) -> bool:
    """
    Return *True* if the string in *cmd* can be run by a shell or *False* if it's just a string
    """
    return any(c.isspace() for c in cmd)


def run_shell_cmd(cmd: str) -> str:
    """"""
    return subprocess.getoutput(cmd)


def add_cls_str_for_cache(cls: T.Any) -> T.Any:
    def _str_fcn(self: T.Any) -> str:
        return (
            f"<{self.__class__.__name__} " + ", ".join([f"{k}={v}" for k, v in self.Schema().dump(self).items()]) + ">"
        )

    cls.__str__ = _str_fcn

    return cls


@add_cls_str_for_cache
@add_schema
@dataclass(frozen=True, eq=True, repr=False)
class StaticEndpoint:
    """
    Point to a static release or use custom commands
    """

    url_cmd: str = ""
    """
    """
    ver_cmd: str = ""
    """
    """

    Schema: T.ClassVar[T.Type[ma.Schema]] = ma.Schema

    class Meta:
        ordered = True

    @ma.pre_load
    def set_defaults(self, in_data: "GitHubRelease", **kwargs: T.Any) -> "GitHubRelease":
        # TODO set to a command if is just a hard-coded string
        # TODO if url_cmd or ver_cmd are hard - coded URLS, substitute with a command: echo "url"
        print("todo!")
        # if not in_data.name and in_data.json_path.is_file():
        #     in_data.name = in_data.json_path.parent.name

        return in_data


@add_cls_str_for_cache
@add_schema
@dataclass(frozen=True, eq=True, repr=False)
class GitHubRelease:
    """Get a URL from the latest gihub release"""

    orgrepo: str
    """
    Github "organization/repository"
    """
    filters: T.Sequence[str] = field(default_factory=tuple)
    """
    How to grep the release JSON to get the version you want
    """

    Schema: T.ClassVar[T.Type[ma.Schema]] = ma.Schema

    class Meta:
        ordered = True

    @ma.pre_load
    def set_defaults(self, in_data: dict[T.Any, T.Any], **kwargs: T.Any) -> dict[T.Any, T.Any]:
        # URL escapes
        in_data["orgrepo"] = url_quote(in_data.get("orgrepo", ""))

        # TODO Shell escapes (careful with this, breaks with uml\\.jar\"
        # in_data["filters"] = tuple(sh_quote(f) for f in in_data.get("filters", tuple()))

        return in_data

    @property
    def ver_cmd(self) -> str:
        """
        TODO assert curl installed...
        """
        return f"curl -Ls -o /dev/null -w %{{url_effective}} https://github.com/{self.orgrepo}/releases/latest | rev | cut -d/ -f1 | rev"

    @property
    def url_cmd(self) -> str:
        """
        *orgrepo* should be organization/repository (eg. cheat/cheat)
        requires:
        - curl
        - jq
        """
        cmd = f"curl --silent 'https://api.github.com/repos/{self.orgrepo}/releases/latest' | jq '..|.browser_download_url?'"
        cmd += "".join(f" | grep '{f}'" for f in self.filters)
        cmd += " | tr -d '\"'"
        return cmd


ENDPOINT_KEYMAP = {
    c: c.__dataclass_fields__.keys()  # type: ignore[attr-defined]
    for c in (
        StaticEndpoint,
        GitHubRelease,
    )
}

# Safety check...
for e_type in ENDPOINT_KEYMAP:
    for method_name in ("url_cmd", "ver_cmd"):
        assert hasattr(e_type, method_name)


class PkgDownloadField(PolyFieldBase):  # type: ignore[misc]
    """ """

    cls_by_length = sorted(ENDPOINT_KEYMAP, key=lambda k: len(ENDPOINT_KEYMAP[k]))

    def serialization_schema_selector(self, value: T.Any, obj: T.Any) -> ma.Schema:
        return value.Schema()

    def deserialization_schema_selector(self, value: dict[T.Any, T.Any], obj: T.Any) -> ma.Schema:
        """Get the correct schema based on the *cls* field"""

        input_keys = set(value.keys())
        for cls in self.cls_by_length:
            keys = set(ENDPOINT_KEYMAP[cls]).difference(
                {
                    "Schema",
                }
            )
            if input_keys == keys:
                return cls.Schema()  # type: ignore[attr-defined]
        raise KeyError(f"unknown Endpoint: {value}")


class _PkgDownloadInterface(T.NamedTuple):
    ver_cmd: str
    url_cmd: str


PkgDownload = NewType("PkgDownload", _PkgDownloadInterface, field=PkgDownloadField)


@add_schema
@dataclass(repr=False)
class PkgDownloadSourcesCache:
    """ """

    source_hash: str = ""
    """
    """
    url: str = ""
    """
    """
    archive_ext: str = ""
    """
    """

    Schema: T.ClassVar[T.Type[ma.Schema]] = ma.Schema

    class Meta:
        ordered = True


@add_schema
@dataclass(repr=False)
class PkgDownloadSources:
    """
    Holds the information required to resolve a URL
    LIST OF SOURCES IN ORDER OF PRIORITY
    """

    sources: list[PkgDownload] = field(default_factory=list)
    """
    """
    cache: PkgDownloadSourcesCache = field(default_factory=PkgDownloadSourcesCache)
    """
    If it changes, get the extension again
    """
    Schema: T.ClassVar[T.Type[ma.Schema]] = ma.Schema

    class Meta:
        ordered = True

    # @ma.post_dump
    # def clean_list(self, in_data: "PkgDownloadSources", **kwargs: T.Any) -> "PkgDownloadSources":
    #     """
    #     TODO
    #     Remove empty blocks
    #     """
    #     return in_data

    @property
    def source(self) -> "PkgDownload":
        """
        TODO PRIORITY
        """
        return self.sources[0]

    @property
    def cog_args(self) -> dict[str, str]:
        """
        TODO add caching in JSON? Has to be written to JSON file to persist!
        """
        try:
            source = self.source
        except IndexError:
            self.cache = PkgDownloadSourcesCache()
            return dict(
                URL_CMD="",
                URL="",
                ARCHIVE_EXT="",
                VER_CMD="",
            )
        ver_cmd = source.ver_cmd
        url_cmd = source.url_cmd

        source_hash = str(source)
        if not self.cache or self.cache.source_hash != source_hash:
            logger.debug(f"Updating cache for {source}")
            self.cache.source_hash = source_hash
            self.cache.url = run_shell_cmd(url_cmd)
            try:
                self.cache.archive_ext = ARCHIVE_EXTS.match(self.cache.url)
            except KeyError:
                pass

        return dict(
            URL_CMD=url_cmd,
            URL=self.cache.url,
            ARCHIVE_EXT=self.cache.archive_ext,
            VER_CMD=ver_cmd,
        )
