#!/bin/bash

# <<<AUTOGENERATED - DO NOT MODIFY>>>
#		 >     File: upstream-ver.sh
#		 >     Name: tidal-hifi
#		 > Template: flatpak

printf "com.mastermindzh.tidal-hifi > %s\n" "$(flatpak search com.mastermindzh.tidal-hifi | head -n1 | cut -f4 | tr -d /" /")"
