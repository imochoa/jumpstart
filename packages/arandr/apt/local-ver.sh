#!/bin/bash
set -euo pipefail
IFS=$'\n\t'

# <<<AUTOGENERATED - DO NOT MODIFY>>>
#		 >     File: local-ver.sh
#		 >     Name: arandr
#		 > Template: apt

printf "arandr > %s\n" "$(apt-cache policy arandr | grep Installed | cut -d: -f2 | tr -d /" /")"
