#!/usr/bin/env sh
# <<<AUTOGENERATED - DO NOT MODIFY>>>
#		 >     File: local-ver.sh
#		 >     Name: doas
#		 > Template: apt

printf "doas > %s\n" "$(apt-cache policy doas | grep Installed | cut -d: -f2 | tr -d /" /")"
