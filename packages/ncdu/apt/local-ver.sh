#!/bin/bash
set -euo pipefail
IFS=$'\n\t'

# <<<AUTOGENERATED - DO NOT MODIFY>>>
#		 >     File: local-ver.sh
#		 >     Name: ncdu
#		 > Template: apt

printf "ncdu > %s\n" "$(apt-cache policy ncdu | grep Installed | cut -d: -f2 | tr -d /" /")"
