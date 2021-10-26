#!/usr/bin/env python3

# stdlib imports
from distutils.core import setup
import os

# REPO_DIR = os.path.dirname(__file__)
# with open(os.path.join(REPO_DIR, "requirements.txt")) as f:
#     requirements = f.read().splitlines()
#
# scripts = [os.path.join("bin", s) for s in os.listdir(os.path.join(REPO_DIR, "bin"))]
#
# with open(os.path.join(REPO_DIR, "README.md")) as f:
#     long_description = f.read().splitlines()

# scripts = scripts,

setup(
    name="jumpstart",
    version="1.0.0",
    packages=[
        "jumpstart",
    ],
    entry_points={
        "console_scripts": [
            "report = jumpstart.cli_fcns:report",
            "refresh = jumpstart.cli_fcns:refresh",
        ],
    },
    license="MIT",
    # install_requires=requirements,
)
