#!/usr/bin/env sh
# <<<AUTOGENERATED - DO NOT MODIFY>>>
#		 > LOCAL-VER.SH
#		 > Sys
#		 > apt

printf "sysprof > %s\n" "$(apt-cache policy sysprof | grep Installed | cut -d: -f2 | tr -d /" /")"
