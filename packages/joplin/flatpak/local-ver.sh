#!/usr/bin/env sh
# <<<AUTOGENERATED - DO NOT MODIFY>>>
#		 >     File: local-ver.sh
#		 >     Name: Joplin
#		 > Template: flatpak

printf "net.cozic.joplin_desktop > %s\n" "$(flatpak info net.cozic.joplin_desktop | grep Version | cut -d: -f2 | tr -d /" /")"
