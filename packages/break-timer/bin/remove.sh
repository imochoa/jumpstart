#!/bin/bash
set -euo pipefail
IFS=$'\n\t'

# <<<AUTOGENERATED - DO NOT MODIFY>>>
#		 >     File: remove.sh
#		 >     Name: Break Timer
#		 > Template: bin

# Variables


# Commands
( [ -f "${INSTALL_DST}/breaktimer" ] && sudo rm "${INSTALL_DST}/breaktimer" || echo "${INSTALL_DST}/breaktimer does not exist" )
