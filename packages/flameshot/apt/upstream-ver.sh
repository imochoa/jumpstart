#!/usr/bin/env sh
# <<<AUTOGENERATED - DO NOT MODIFY>>>
#		 > UPSTREAM-VER.SH
#		 > flameshot
#		 > apt

printf "flameshot > %s\n" "$(apt-cache policy flameshot | grep Candidate | cut -d: -f2 | tr -d /" /")"