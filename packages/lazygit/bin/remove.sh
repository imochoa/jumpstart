#!/bin/bash
set -euo pipefail
IFS=$'\n\t'

# <<<AUTOGENERATED - DO NOT MODIFY>>>
#		 >     File: remove.sh
#		 >     Name: LazyGit
#		 > Template: bin

# Variables


# Commands
( [ -f "${INSTALL_DST}/lazygit" ] && sudo rm "${INSTALL_DST}/lazygit" || echo "${INSTALL_DST}/lazygit does not exist" )
