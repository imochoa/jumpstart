#!/usr/bin/env sh
# <<<AUTOGENERATED - DO NOT MODIFY>>>
#		 > LOCAL-VER.SH
#		 > xournalpp
#		 > apt

printf "xournalpp > %s\n" "$(apt-cache policy xournalpp | grep Installed | cut -d: -f2 | tr -d /" /")"