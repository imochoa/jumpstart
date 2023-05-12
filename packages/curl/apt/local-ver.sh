#!/bin/bash
set -euo pipefail
IFS=$'\n\t'

# <<<AUTOGENERATED - DO NOT MODIFY>>>
#		 >     File: local-ver.sh
#		 >     Name: curl
#		 > Template: apt

printf "curl > %s\n" "$(apt-cache policy curl | grep Installed | cut -d: -f2 | tr -d /" /")"
