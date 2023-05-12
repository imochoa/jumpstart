#!/bin/bash
set -euo pipefail
IFS=$'\n\t'

# <<<AUTOGENERATED - DO NOT MODIFY>>>
#		 >     File: upstream-ver.sh
#		 >     Name: Live Captions
#		 > Template: apt

printf "blender > %s\n" "$(apt-cache policy blender | grep Candidate | cut -d: -f2 | tr -d /" /")"
