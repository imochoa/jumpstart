#!/usr/bin/env sh
# <<<AUTOGENERATED - DO NOT MODIFY>>>
#		 >     File: local-ver.sh
#		 >     Name: Sys
#		 > Template: apt

printf "sysprof > %s\n" "$(apt-cache policy sysprof | grep Installed | cut -d: -f2 | tr -d /" /")"
