#!/usr/bin/env sh
# <<<AUTOGENERATED - DO NOT MODIFY>>>
#		 > LOCAL-VER.SH
#		 > ncdu
#		 > apt

printf "ncdu > %s\n" "$(apt-cache policy ncdu | grep Installed | cut -d: -f2 | tr -d /" /")"
