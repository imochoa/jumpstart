#!/usr/bin/env sh
# <<<AUTOGENERATED - DO NOT MODIFY>>>
#		 >     File: local-ver.sh
#		 >     Name: meld
#		 > Template: apt

printf "meld > %s\n" "$(apt-cache policy meld | grep Installed | cut -d: -f2 | tr -d /" /")"
