#!/bin/bash
set -euo pipefail
IFS=$'\n\t'

# <<<AUTOGENERATED - DO NOT MODIFY>>>
#		 >     File: local-ver.sh
#		 >     Name: gparted
#		 > Template: apt

printf "gparted > %s\n" "$(apt-cache policy gparted | grep Installed | cut -d: -f2 | tr -d /" /")"
