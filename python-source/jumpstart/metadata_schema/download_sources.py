#!/usr/bin/env python3

# stdlib imports
from dataclasses import dataclass, field
import pathlib
import typing as T

import urllib.parse
import re
# 3rd party imports
from loguru import logger
import marshmallow as ma
from marshmallow_dataclass import add_schema


@add_schema
@dataclass
class GithubRelease:
    """For downloading from a github release"""

    repo: str
    filter_args: T.List[str] = field(default_factory=list)
    Schema: T.ClassVar[T.Type[ma.Schema]] = ma.Schema

    class Meta:
        ordered = True


    def __post_init__(self) -> None:
        """
        1. Perform safety checks
        """
        assert urllib.parse.quote(self.repo) == self.repo, f"Invalid github repo: {self.repo}. Non-URL chars"
        assert len(self.repo.split('/')) == 1, f"Invalid github repo: {self.repo}. Missing '/'"
        
    def resolve_url(self)->str:
        print("HOHO")

        return ''

    @property
    def urlrlrl(self):
        # URL =$(curl - -silent "https://api.github.com/repos/sharkdp/fd/releases/latest" \
        #     | jq '..|.browser_download_url?' | grep 'x86_64' | grep 'linux' | grep 'gnu' \
        #     | tr -d '"')
        return ''


@add_schema
@dataclass
class DownloadSource:
    """"""

    static_url: str = field(default="")
    github_release: T.Optional[GithubRelease] = None
    url: str = field(default="", metadata=dict(data_key="url_post_resolution"))
    Schema: T.ClassVar[T.Type[ma.Schema]] = ma.Schema

    class Meta:
        ordered = True

    def __post_init__(self: "DownloadSource") -> None:
        """
        1. Perform safety checks
        2. Determine self.url attribute automatically based on the other attributes
        """

        # Clean up static url
        self.static_url = self.static_url.strip()
        self.static_url =re.sub(r'https?\://','',self.static_url)
        self.static_url = 'https://'+urllib.parse.quote(self.static_url)

        # Determine the URL
        old_url = self.url
        self.url = self.resolve_url()

        if old_url!=self.url:
            logger.info(f"Updated the URL for {self}")





        print("CLEAN!")

        if not self.static_url:
            self.update_static_url()

            # TODO cleanups! strip http:// and re-add it!
            # self.static_url = urllib.parse.quote(self.static_url)
            # TODO SHell escape as wellAlternative!
            self.url = self.static_url
    def resolve_url(self)->str:
        
        # Priority
        if self.static_url:
            return self.static_url
        if self.github_release:
            return self.github_release.resolve_url()
        
        raise AttributeError("Could not resolve")
        
        print("HOHO")
