#!/usr/bin/env sh
# <<<AUTOGENERATED - DO NOT MODIFY>>>
#		 > UPSTREAM-VER.SH
#		 > Flatpak
#		 > apt

printf "flatpak > %s\n" "$(apt-cache policy flatpak | grep Candidate | cut -d: -f2 | tr -d /" /")"
printf "gnome-software-plugin-flatpak > %s\n" "$(apt-cache policy gnome-software-plugin-flatpak | grep Candidate | cut -d: -f2 | tr -d /" /")"
