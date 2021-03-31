#!/bin/bash

# COLORS
RED='\033[0;31m'
BLUE='\033[0;34m'
CYAN='\033[0;36m' #0;36
NC='\033[0m' # No Color

# SETUP
BINDIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" >/dev/null 2>&1 && pwd)"
REPODIR=$(realpath "${BINDIR}/..")
DOTFILEDIR="${REPODIR}/dotfiles"

# HELPER FCN

function dl () { # Expects "NAME" then "URL"
  local fpath="$(find ${DOTFILEDIR} -type f -iname $1)"
  echo -e "\n${CYAN}Attempting '$1' ... \n${NC}";
  curl --silent --show-error "$2" > $fpath || echo -e "\n${RED}Getting '$1' FAILED\n${NC}"
  # notify-send -u "critical" "$1 FAILED"
}


echo -e "${BLUE}\n\nGetting the autocompletion files...\n\n${NC}";

dl 'cheat.bash' \
'https://raw.githubusercontent.com/cheat/cheat/master/scripts/cheat.bash'

dl 'docker.bash' \
"https://raw.githubusercontent.com/docker/cli/v$(docker version --format '{{.Server.Version}}' | sed 's/-.*//')/contrib/completion/bash/docker"
dl 'docker-compose.bash' \
"https://raw.githubusercontent.com/docker/compose/$(docker-compose version --short)/contrib/completion/bash/docker-compose"


echo -e "${RED}\n\nGetting the NVIM files...\n\n${NC}";
dl 'nvim_desktop_wrapper.py' 'https://raw.githubusercontent.com/fmoralesc/neovim-gnome-terminal-wrapper/master/nvim-wrapper'
## https://raw.githubusercontent.com/fmoralesc/neovim-gnome-terminal-wrapper/master/neovim.desktop
## https://raw.githubusercontent.com/fmoralesc/neovim-gnome-terminal-wrapper/master/neovim.svg


# cb
# https://gist.githubusercontent.com/bendangelo/4061436/raw/73dc70d75bb2758d4bcc98a6e4fd4ebf87b8a9a3/xclip
