#!/bin/bash
set -euo pipefail
IFS=$'\n\t'

# <<<AUTOGENERATED - DO NOT MODIFY>>>
#		 >     File: local-ver.sh
#		 >     Name: bat
#		 > Template: apt

printf "bat > %s\n" "$(apt-cache policy bat | grep Installed | cut -d: -f2 | tr -d /" /")"
