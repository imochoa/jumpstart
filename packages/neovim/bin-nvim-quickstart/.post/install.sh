# [[[cog
# import cog
# from jumpstart.cogging import OSPaths
# from jumpstart.cogging.helpers import str2list, require_cmds, chain_cmds, printf, wget, curl
# from jumpstart.templates.bin.bin_cog_utils import install_bin
#
# p1_cmd=printf("Download_icon")
# icon_url="https://raw.githubusercontent.com/neovim/neovim.github.io/master/logos/neovim-mark.svg"
# icon_wget_cmd=wget(url=icon_url,dst=OSPaths.debian.icons.g + "/neovim",as_root=True)
# cog.outl(chain_cmds([p1_cmd,icon_wget_cmd]))
#
#
# p2_cmd=printf("Download kickstart nvim init.lua")
# init_url="https://raw.githubusercontent.com/nvim-lua/kickstart.nvim/master/init.lua"
# init_curl_cmd=curl(url=init_url,dst="${HOME}/.config/nvim/init.lua")
# cog.outl(chain_cmds([p2_cmd,init_curl_cmd]))
#
# ]]]
# [[[end]]]

# Set up config dir
mkdir -p ${HOME}/.config/nvim
cd ${HOME}/.config/nvim

# Run :PackerInstall
# Start nvim and run `:PackerInstall` (ignore the errors)
nvim --headless -c 'autocmd User PackerComplete quitall' -c 'PackerSync'

# Restart neovim -> install plugins
# Restart neovim -> install LSPs
