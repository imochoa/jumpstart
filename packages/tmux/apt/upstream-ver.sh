#!/usr/bin/env sh
# <<<AUTOGENERATED - DO NOT MODIFY>>>
#		 > UPSTREAM-VER.SH
#		 > tmux
#		 > apt

printf "tmux > %s\n" "$(apt-cache policy tmux | grep Candidate | cut -d: -f2 | tr -d /" /")"
