#!/usr/bin/env sh
# <<<AUTOGENERATED - DO NOT MODIFY>>>
#		 > LOCAL-VER.SH
#		 > KeePassXC
#		 > flatpak

printf "org.keepassxc.KeePassXC > %s\n" "$(flatpak info org.keepassxc.KeePassXC | grep Version | cut -d: -f2 | tr -d /" /")"
