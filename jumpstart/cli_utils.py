#! /usr/bin/env python3

# std imports
# stdlib imports
from enum import Enum
import sys
import typing as T


class bcolors(Enum):
    BLUE = "\033[94m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    ENDC = "\033[0m"

    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"


def colorize(msg: str, color: bcolors) -> str:
    return f"{color}{msg}{bcolors.ENDC}"


def debug(msg: str) -> None:
    sys.stdout.write(f"{bcolors.BLUE}{msg}{bcolors.ENDC}\n")


def info(msg: str) -> None:
    sys.stdout.write(f"{bcolors.GREEN}{msg}{bcolors.ENDC}\n")


def warning(msg: str) -> None:
    sys.stdout.write(f"{bcolors.YELLOW}{msg}{bcolors.ENDC}\n")


def error(msg: str) -> None:
    sys.stdout.write(f"{bcolors.RED}{msg}{bcolors.ENDC}\n")


if __name__ == "__main__":
    debug("debug msg")
    info("info msg")
    warning("warning msg")
    error("error msg")
