#!/usr/bin/env python3

"""
Only meant to be imported within cog
"""

# local imports
from .cmds import chain_cmds, printf, require_cmds, tempdir_cmd
from .constants import HEADER, POST_HEADER, PRINTF_FMT, SCRIPT_DEFAULTS, SH_SHEBANG
from .github import find_github_release, find_github_version
from .utils import safedelete, sh_escape, str2dict, str2list
