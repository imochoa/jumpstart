#!/usr/bin/env sh
# <<<AUTOGENERATED - DO NOT MODIFY>>>
#		 > LOCAL-VER.SH
#		 > httrack
#		 > apt

printf "webhttrack > %s\n" "$(apt-cache policy webhttrack | grep Installed | cut -d: -f2 | tr -d /" /")"
