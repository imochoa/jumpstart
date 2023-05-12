#!/bin/bash
set -euo pipefail
IFS=$'\n\t'

# <<<AUTOGENERATED - DO NOT MODIFY>>>
#		 >     File: local-ver.sh
#		 >     Name: lua
#		 > Template: apt

printf "lua5.3 > %s\n" "$(apt-cache policy lua5.3 | grep Installed | cut -d: -f2 | tr -d /" /")"
printf "luarocks > %s\n" "$(apt-cache policy luarocks | grep Installed | cut -d: -f2 | tr -d /" /")"
printf "luajit > %s\n" "$(apt-cache policy luajit | grep Installed | cut -d: -f2 | tr -d /" /")"
