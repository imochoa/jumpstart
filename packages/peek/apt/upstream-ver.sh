#!/usr/bin/env sh
# <<<AUTOGENERATED - DO NOT MODIFY>>>
#		 >     File: upstream-ver.sh
#		 >     Name: peek
#		 > Template: apt

printf "peek > %s\n" "$(apt-cache policy peek | grep Candidate | cut -d: -f2 | tr -d /" /")"
