#!/usr/bin/env sh
# <<<AUTOGENERATED - DO NOT MODIFY>>>
#		 > UPSTREAM-VER.SH
#		 > screenkey
#		 > apt

printf "screenkey > %s\n" "$(apt-cache policy screenkey | grep Candidate | cut -d: -f2 | tr -d /" /")"
