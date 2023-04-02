# [[[cog
# import cog
# from jumpstart.cogging.helpers import str2list, require_cmds, chain_cmds, printf
# from jumpstart.templates.bin.bin_cog_utils import install_bin
#
# ]]]
# [[[end]]]
#

# TODO!
# Install neovim

# Set up config dir
mkdir -p ~/.config/nvim
cd ~/.config/nvim

# Copy kickstart.nvim
curl -JL "https://raw.githubusercontent.com/nvim-lua/kickstart.nvim/master/init.lua" -o "${HOME}/.config/nvim/init.lua"

# Run :PackerInstall
# Start nvim and run `:PackerInstall` (ignore the errors)
nvim --headless -c 'autocmd User PackerComplete quitall' -c 'PackerSync'

# Restart neovim -> install plugins
# Restart neovim -> install LSPs
