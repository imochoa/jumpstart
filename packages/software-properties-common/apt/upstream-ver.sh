#!/usr/bin/env sh
# <<<AUTOGENERATED - DO NOT MODIFY>>>
#		 >     File: upstream-ver.sh
#		 >     Name: software-properties-common
#		 > Template: apt

printf "software-properties-common > %s\n" "$(apt-cache policy software-properties-common | grep Candidate | cut -d: -f2 | tr -d /" /")"
