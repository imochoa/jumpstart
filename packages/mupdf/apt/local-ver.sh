#!/usr/bin/env sh
# <<<AUTOGENERATED - DO NOT MODIFY>>>
#		 > LOCAL-VER.SH
#		 > mupdf
#		 > apt

printf "mupdf > %s\n" "$(apt-cache policy mupdf | grep Installed | cut -d: -f2 | tr -d /" /")"
