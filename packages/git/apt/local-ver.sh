#!/bin/bash
set -euo pipefail
IFS=$'\n\t'

# <<<AUTOGENERATED - DO NOT MODIFY>>>
#		 >     File: local-ver.sh
#		 >     Name: git
#		 > Template: apt

printf "git > %s\n" "$(apt-cache policy git | grep Installed | cut -d: -f2 | tr -d /" /")"
