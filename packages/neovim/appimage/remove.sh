#!/bin/bash
set -euo pipefail
IFS=$'\n\t'

# <<<AUTOGENERATED - DO NOT MODIFY>>>
#		 >     File: remove.sh
#		 >     Name: neovim
#		 > Template: bin

# Variables


# Commands
( [ -f "${INSTALL_DST}/nvim" ] && sudo rm "${INSTALL_DST}/nvim" || echo "${INSTALL_DST}/nvim does not exist" )
