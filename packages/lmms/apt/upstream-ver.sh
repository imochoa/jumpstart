#!/usr/bin/env sh
# <<<AUTOGENERATED - DO NOT MODIFY>>>
#		 >     File: upstream-ver.sh
#		 >     Name: lmms
#		 > Template: apt

printf "lmms > %s\n" "$(apt-cache policy lmms | grep Candidate | cut -d: -f2 | tr -d /" /")"
