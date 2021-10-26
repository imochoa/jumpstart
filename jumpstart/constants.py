#!/usr/bin/env python3

# stdlib imports
from enum import Enum
import logging
import pathlib
import platform
import subprocess

# This sets the root logger to write to stdout (your console).
# Your script/app needs to call this somewhere at least once.
logging.basicConfig()

# By default the root logger is set to WARNING and all loggers you define
# inherit that value. Here we set the root logger to NOTSET. This logging
# level is automatically inherited by all existing and new sub-loggers
# that do not set a less verbose level.
logging.root.setLevel(logging.NOTSET)

# The following line sets the root logger level as well.
# It's equivalent to both previous statements combined:
logging.basicConfig(level=logging.NOTSET)


# You can either share the `logger` object between all your files or the
# name handle (here `my-app`) and call `logging.getLogger` with it.
# The result is the same.
# handle = "my-app"
# logger1 = logging.getLogger(handle)
# logger2 = logging.getLogger(handle)
# logger1 and logger2 point to the same object:
# (logger1 is logger2) == True

logger = logging.getLogger(__name__)
# logger = logging.getLogger("my-app")
# # Convenient methods in order of verbosity from highest to lowest
# logger.debug("this will get printed")
# logger.info("this will get printed")
# logger.warning("this will get printed")
# logger.error("this will get printed")
# logger.critical("this will get printed")


# In large applications where you would like more control over the logging,
# create sub-loggers from your main application logger.
component_logger = logger.getChild("component-a")
component_logger.info("this will get printed with the prefix `my-app.component-a`")

# If you wish to control the logging levels, you can set the level anywhere
# in the hierarchy:
#
# - root
#   - my-app
#     - component-a
#

# Example for development:
logger.setLevel(logging.DEBUG)

# If that prints too much, enable debug printing only for your component:
component_logger.setLevel(logging.DEBUG)


# # For production you rather want:
# logger.setLevel(logging.WARNING)


# Paths
PKG_DIR = pathlib.Path(__file__).parent
REPO_DIR = (PKG_DIR / "..").resolve()
INDEX_DIR = REPO_DIR / "index"

LINUX = "Linux"
SUPPORTED_SYSTEMS = {
    "Linux",
}


class Architecture(Enum):
    unknown = "unknown"
    x64 = "x64"
    arm = "arm"


# Architecture?
DETECTED_ARCH: Architecture = Architecture.unknown
if platform.machine().endswith("64"):
    DETECTED_ARCH = Architecture.x64
elif platform.machine().endswith("arm"):
    # TODO?
    DETECTED_ARCH = Architecture.arm
logger.info(f"Auto-detected architecture: {DETECTED_ARCH}")


class System(Enum):
    unknown = "unknown"
    linux = "Linux"


DETECTED_SYSTEM = System(platform.system())
logger.info(f"Auto-detected system: {DETECTED_ARCH}")


class OperatingSystem(Enum):
    unknown = "unknown"
    ubuntu2004 = "ubuntu2004"


DETECTED_OS = "NONE"
if DETECTED_SYSTEM == System.linux:
    p_stdout = subprocess.check_output(["lsb_release", "-a"])
    if p_stdout:
        DETECTED_OS = p_stdout.decode("utf8").split("\n")[1].split(":")[1].strip()
logger.info(f"Auto-detected OS: {DETECTED_OS}")
