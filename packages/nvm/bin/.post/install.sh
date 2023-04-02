# [[[cog
# import cog
# from jumpstart.cogging.helpers import str2list, require_cmds, chain_cmds, printf
# from jumpstart.templates.bin.bin_cog_utils import install_bin
#
# ]]]
# [[[end]]]
#


# https://github.com/nvm-sh/nvm
# ToDo get latest? and not 0.39.3
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.3/install.sh | bash

# Deeper shell integration
# https://github.com/nvm-sh/nvm#deeper-shell-integration

# Update ?
nvm install-latest-npm

# Install node ?
nvm install --lts
