#!/usr/bin/env sh
# <<<AUTOGENERATED - DO NOT MODIFY>>>
#		 > LOCAL-VER.SH
#		 > suckless-tools
#		 > apt

printf "suckless-tools > %s\n" "$(apt-cache policy suckless-tools | grep Installed | cut -d: -f2 | tr -d /" /")"
