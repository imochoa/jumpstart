#!/usr/bin/env sh
# <<<AUTOGENERATED - DO NOT MODIFY>>>
#		 >     File: upstream-ver.sh
#		 >     Name: shellcheck
#		 > Template: apt

printf "shellcheck > %s\n" "$(apt-cache policy shellcheck | grep Candidate | cut -d: -f2 | tr -d /" /")"
