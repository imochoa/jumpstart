#!/bin/bash
set -euo pipefail
IFS=$'\n\t'

# <<<AUTOGENERATED - DO NOT MODIFY>>>
#		 >     File: upstream-ver.sh
#		 >     Name: wget
#		 > Template: apt

printf "wget > %s\n" "$(apt-cache policy wget | grep Candidate | cut -d: -f2 | tr -d /" /")"
