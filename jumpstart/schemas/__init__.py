#!/usr/bin/env python3

# stdlib imports
import codecs
import json
from pathlib import Path
import typing as T

# 3rd party imports
import marshmallow

# local imports
from .metadata import PackageMetadata


def load_json(
    p: Path,
) -> dict[str, T.Any]:
    with codecs.open(
        str(p.absolute()),
        "r",
        encoding="utf-8",
        errors="ignore",
    ) as fp:
        obj = json.load(fp)
    return obj


def dump_json(
    p: Path,
    obj: dict[str, T.Any],
) -> None:
    with codecs.open(
        str(p.absolute()),
        "w",
        encoding="utf-8",
        errors="ignore",
    ) as fp:
        json.dump(
            obj=obj,
            fp=fp,
            indent=2,
        )

    return None
