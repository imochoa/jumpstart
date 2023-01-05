#!/usr/bin/env python3

"""
Only meant to be imported within cog
"""

# local imports
from .cmds import chain_cmds, printf, require_cmds, tempdir_cmd
from .constants import HEADER, POST_HEADER, PRINTF_FMT, SCRIPT_DEFAULTS, SH_SHEBANG
from .utils import safedelete, str2list
