#!/usr/bin/env sh
# <<<AUTOGENERATED - DO NOT MODIFY>>>
#		 >     File: upstream-ver.sh
#		 >     Name: arandr
#		 > Template: apt

printf "arandr > %s\n" "$(apt-cache policy arandr | grep Candidate | cut -d: -f2 | tr -d /" /")"
