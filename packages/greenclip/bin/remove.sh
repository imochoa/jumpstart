#!/bin/bash
set -euo pipefail
IFS=$'\n\t'

# <<<AUTOGENERATED - DO NOT MODIFY>>>
#		 >     File: remove.sh
#		 >     Name: greenclip
#		 > Template: bin

# Variables


# Commands
( [ -f "${INSTALL_DST}/greenclip" ] && sudo rm "${INSTALL_DST}/greenclip" || echo "${INSTALL_DST}/greenclip does not exist" )
