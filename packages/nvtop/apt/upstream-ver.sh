#!/usr/bin/env sh
# <<<AUTOGENERATED - DO NOT MODIFY>>>
#		 > UPSTREAM-VER.SH
#		 > nvtop
#		 > apt

printf "nvtop > %s\n" "$(apt-cache policy nvtop | grep Candidate | cut -d: -f2 | tr -d /" /")"