#!/usr/bin/env sh
# <<<AUTOGENERATED - DO NOT MODIFY>>>
#		 > LOCAL-VER.SH
#		 > bat
#		 > apt

printf "bat > %s\n" "$(apt-cache policy bat | grep Installed | cut -d: -f2 | tr -d /" /")"
