#!/usr/bin/env sh
# <<<AUTOGENERATED - DO NOT MODIFY>>>
#		 >     File: upstream-ver.sh
#		 >     Name: git
#		 > Template: apt

printf "git > %s\n" "$(apt-cache policy git | grep Candidate | cut -d: -f2 | tr -d /" /")"
