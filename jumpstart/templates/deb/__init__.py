# stdlib imports
from dataclasses import dataclass, field
import json
import typing as T

# 3rd party imports
import marshmallow as ma
from marshmallow_dataclass import add_schema

# 1st party imports
from jumpstart.schemas.params_header import ParamsHeader
from jumpstart.schemas.pkg_download import PkgDownloadSources
from jumpstart.schemas.schema_utils import dump_json


@add_schema
@dataclass(repr=False)
class DebParams:
    """
    For one .deb file
    """

    header: ParamsHeader
    """
    Should be one of....
    """
    download_sources: PkgDownloadSources
    """
    """
    Schema: T.ClassVar[T.Type[ma.Schema]] = ma.Schema

    class Meta:
        ordered = True
        # exclude = ("cmdname",)

    @property
    def cog_args(self) -> dict[str, str]:
        # Update download sources cache?
        past_hash = self.download_sources.cache.source_hash
        download_sources_cog_args = self.download_sources.cog_args
        if (
            past_hash != self.download_sources.cache.source_hash
            and self.header.json_path
            and self.header.json_path.is_file()
        ):
            dump_json(self.header.json_path, obj=self.Schema().dump(self))

        return {
            **dict(
                # CMDMAP=json.dumps(self.cmdmap),
            ),
            **download_sources_cog_args,
        }
