#!/usr/bin/env python3

# stdlib imports
from distutils.core import setup
import pathlib

REPO_DIR = pathlib.Path(__file__).absolute().parent
with open(str(REPO_DIR / "requirements.txt")) as f:
    requirements = [line.strip() for line in f.read().splitlines()]
    requirements = [line for line in requirements if not line.startswith("#")]

# scripts = [os.path.join("bin", s) for s in os.listdir(os.path.join(REPO_DIR, "bin"))]

with open(REPO_DIR / "README.md") as f:
    long_description = f.read().splitlines()

setup(
    name="jumpstart",
    version="1.0.0",
    packages=[
        "jumpstart",
    ],
    entry_points={
        "console_scripts": [
            "jumpstart = jumpstart.cli_fcns:jumpstart",
        ],
    },
    license="MIT",
    install_requires=requirements,
)
