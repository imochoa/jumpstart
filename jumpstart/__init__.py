#!/usr/bin/env python3
import enum
import pathlib

PKG_DIR = pathlib.Path(__file__).parent
REPO_DIR = (PKG_DIR / "..").resolve()
INDEX_DIR = REPO_DIR / "index"

KNOWN_FILENAMES = {
    "update",
    "install",
    "remove",
    "configure",
    "auto",
    "run",
}


# Important filenames
class AppFilenames(enum.Enum):
    install = "install"
    remove = "remove"
    update = "update"
    status = "status"
