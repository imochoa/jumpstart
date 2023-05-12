#!/bin/bash
set -euo pipefail
IFS=$'\n\t'

# <<<AUTOGENERATED - DO NOT MODIFY>>>
#		 >     File: local-ver.sh
#		 >     Name: sqlite
#		 > Template: apt

printf "sqlite3 > %s\n" "$(apt-cache policy sqlite3 | grep Installed | cut -d: -f2 | tr -d /" /")"
printf "sqlite3-tools > %s\n" "$(apt-cache policy sqlite3-tools | grep Installed | cut -d: -f2 | tr -d /" /")"
printf "sqlitebrowser > %s\n" "$(apt-cache policy sqlitebrowser | grep Installed | cut -d: -f2 | tr -d /" /")"
