#!/usr/bin/env sh
# <<<AUTOGENERATED - DO NOT MODIFY>>>
#		 > UPSTREAM-VER.SH
#		 > Flatseal
#		 > flatpak

printf "com.github.alainm23.planner > %s\n" "$(flatpak search com.github.alainm23.planner | head -n1 | cut -f4 | tr -d /" /")"