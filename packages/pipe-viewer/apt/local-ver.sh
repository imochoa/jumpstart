#!/bin/bash
set -euo pipefail
IFS=$'\n\t'

# <<<AUTOGENERATED - DO NOT MODIFY>>>
#		 >     File: local-ver.sh
#		 >     Name: pipe-viewer
#		 > Template: apt

printf "pv > %s\n" "$(apt-cache policy pv | grep Installed | cut -d: -f2 | tr -d /" /")"
