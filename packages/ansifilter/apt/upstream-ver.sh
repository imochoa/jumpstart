#!/usr/bin/env sh
# <<<AUTOGENERATED - DO NOT MODIFY>>>
#		 >     File: upstream-ver.sh
#		 >     Name: ansifilter
#		 > Template: apt

printf "ansifilter > %s\n" "$(apt-cache policy ansifilter | grep Candidate | cut -d: -f2 | tr -d /" /")"
