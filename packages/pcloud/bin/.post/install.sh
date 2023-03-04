# [[[cog
# import cog
# from cog_utils import str2list, require_cmds, chain_cmds, printf
# from bin_cog_utils import install_bin
#
# ]]]
# [[[end]]]
#

# https://pypa.github.io/pipx/installation/
python3 -m pip install --user pipx
python3 -m pipx ensurepath

# TODO shell completion!
# Follow steps from output of:
# pipx completions