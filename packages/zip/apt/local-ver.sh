#!/bin/bash
set -euo pipefail
IFS=$'\n\t'

# <<<AUTOGENERATED - DO NOT MODIFY>>>
#		 >     File: local-ver.sh
#		 >     Name: zip
#		 > Template: apt

printf "zip > %s\n" "$(apt-cache policy zip | grep Installed | cut -d: -f2 | tr -d /" /")"
printf "unzip > %s\n" "$(apt-cache policy unzip | grep Installed | cut -d: -f2 | tr -d /" /")"
