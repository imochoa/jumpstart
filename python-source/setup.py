#!/usr/bin/env python3

# stdlib imports
import pathlib

# 3rd party imports
import setuptools

PYPKG_DIR = pathlib.Path(__file__).absolute().parent
with open(str(PYPKG_DIR / "requirements.txt")) as f:
    requirements = [line.strip() for line in f.read().splitlines()]
    requirements = [line for line in requirements if not line.startswith("#")]

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
