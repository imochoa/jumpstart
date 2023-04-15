#!/usr/bin/env python3

# stdlib imports
import codecs
import json
from pathlib import Path
import typing as T

# 3rd party imports
import marshmallow as ma


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


def add_cls_name_to_json(cls: T.Any) -> T.Any:
    """
    Automatically extend the Schema with the current class:
    {
        ...
        "cls": NameOfThisClass
        ...
    }
    """

    @ma.post_dump
    def _cls_name_to_json(self: T.Any, data: dict[str, T.Any], **kwargs: T.Any) -> dict[str, T.Any]:
        """ """
        return {**data, **{"cls": type(self).__name__}}

    cls.cls_name_to_json = _cls_name_to_json
    return cls
