#!/usr/bin/env sh
# <<<AUTOGENERATED - DO NOT MODIFY>>>
#		 >     File: local-ver.sh
#		 >     Name: tidal-hifi
#		 > Template: flatpak

printf "com.mastermindzh.tidal-hifi > %s\n" "$(flatpak info com.mastermindzh.tidal-hifi | grep Version | cut -d: -f2 | tr -d /" /")"
