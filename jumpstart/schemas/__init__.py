#!/usr/bin/env python3

# stdlib imports
import codecs
import json
from pathlib import Path
import typing as T

# local imports
from .metadata import PackageMetadata

RT = T.TypeVar("RT")  # return type


def load_json(
    p: Path,
    schema: RT,
) -> RT:
    with codecs.open(
        str(p.absolute()),
        "r",
        encoding="utf-8",
        errors="ignore",
    ) as fp:
        obj = schema.load(json.load(fp))
    return T.cast(RT, obj)


def dump_json(
    p: Path,
    obj: RT,
) -> None:
    with codecs.open(
        str(p.absolute()),
        "w",
        encoding="utf-8",
        errors="ignore",
    ) as fp:
        json.dump(
            obj=obj.Schema().dump(obj),
            fp=fp,
            indent=2,
        )

    return None
