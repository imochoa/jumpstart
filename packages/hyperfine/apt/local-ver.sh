#!/usr/bin/env sh
# <<<AUTOGENERATED - DO NOT MODIFY>>>
#		 > LOCAL-VER.SH
#		 > hyperfine
#		 > apt

printf "hyperfine > %s\n" "$(apt-cache policy hyperfine | grep Installed | cut -d: -f2 | tr -d /" /")"
