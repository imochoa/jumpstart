#!/usr/bin/env sh
# <<<AUTOGENERATED - DO NOT MODIFY>>>
#		 > UPSTREAM-VER.SH
#		 > gnome-tweaks
#		 > apt

printf "gnome-tweak-tool > %s\n" "$(apt-cache policy gnome-tweak-tool | grep Candidate | cut -d: -f2 | tr -d /" /")"
printf "gnome-tweaks > %s\n" "$(apt-cache policy gnome-tweaks | grep Candidate | cut -d: -f2 | tr -d /" /")"