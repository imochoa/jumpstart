#!/usr/bin/env sh
# <<<AUTOGENERATED - DO NOT MODIFY>>>
#		 > UPSTREAM-VER.SH
#		 > pipe-viewer
#		 > apt

printf "pv > %s\n" "$(apt-cache policy pv | grep Candidate | cut -d: -f2 | tr -d /" /")"
