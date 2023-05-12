#!/bin/bash
set -euo pipefail
IFS=$'\n\t'

# <<<AUTOGENERATED - DO NOT MODIFY>>>
#		 >     File: local-ver.sh
#		 >     Name: Live Captions
#		 > Template: apt

printf "blender > %s\n" "$(apt-cache policy blender | grep Installed | cut -d: -f2 | tr -d /" /")"
