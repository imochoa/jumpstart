#!/bin/bash
set -euo pipefail
IFS=$'\n\t'

# <<<AUTOGENERATED - DO NOT MODIFY>>>
#		 >     File: local-ver.sh
#		 >     Name: 7zip
#		 > Template: apt

printf "p7zip-full > %s\n" "$(apt-cache policy p7zip-full | grep Installed | cut -d: -f2 | tr -d /" /")"
printf "p7zip-rar > %s\n" "$(apt-cache policy p7zip-rar | grep Installed | cut -d: -f2 | tr -d /" /")"
