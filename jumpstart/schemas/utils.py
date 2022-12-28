#!/usr/bin/env python3


# stdlib imports
import codecs
import json
from pathlib import Path
import typing as T

# 3rd party imports
import marshmallow as ma

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


def read_template(p: Path) -> str:
    """Given a JSON file, attempt to read the 'template' field"""
    with codecs.open(
        str(p.absolute()),
        "r",
        encoding="utf-8",
        errors="ignore",
    ) as fp:
        obj = json.load(fp)
    return obj.get("template", "")
