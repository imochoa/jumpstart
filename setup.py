#!/usr/bin/env python3

# stdlib imports
import pathlib

# 3rd party imports
import setuptools

REPO_DIR = pathlib.Path(__file__).absolute().parent
with open(str(REPO_DIR / "requirements.txt")) as f:
    requirements = [line.strip() for line in f.read().splitlines()]
    requirements = [line for line in requirements if not line.startswith("#")]

with open(REPO_DIR / "README.md") as f:
    long_description = f.read().splitlines()

setuptools.setup(
    name="jumpstart",
    version="1.0.0",
    packages=setuptools.find_packages(),
    entry_points={
        "console_scripts": [
            "jumpstart = jumpstart.cli:main",
        ],
    },
    license="MIT",
    install_requires=requirements,
)
# package_data = {'index': ['index']},
