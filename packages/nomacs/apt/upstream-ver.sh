#!/usr/bin/env sh
# <<<AUTOGENERATED - DO NOT MODIFY>>>
#		 > UPSTREAM-VER.SH
#		 > nomacs
#		 > apt

printf "gromit-mpx > %s\n" "$(apt-cache policy gromit-mpx | grep Candidate | cut -d: -f2 | tr -d /" /")"
