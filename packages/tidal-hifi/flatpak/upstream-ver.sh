#!/usr/bin/env sh
# <<<AUTOGENERATED - DO NOT MODIFY>>>
#		 > UPSTREAM-VER.SH
#		 > tidal-hifi
#		 > flatpak

printf "com.mastermindzh.tidal-hifi > %s\n" "$(flatpak search com.mastermindzh.tidal-hifi | head -n1 | cut -f4 | tr -d /" /")"