#!/bin/bash
set -euo pipefail
IFS=$'\n\t'

# <<<AUTOGENERATED - DO NOT MODIFY>>>
#		 >     File: local-ver.sh
#		 >     Name: imagemagick
#		 > Template: apt

printf "imagemagick > %s\n" "$(apt-cache policy imagemagick | grep Installed | cut -d: -f2 | tr -d /" /")"
