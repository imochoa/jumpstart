#!/usr/bin/env sh
# <<<AUTOGENERATED - DO NOT MODIFY>>>
#		 >     File: upstream-ver.sh
#		 >     Name: Live Captions
#		 > Template: flatpak

printf "net.sapples.LiveCaptions > %s\n" "$(flatpak search net.sapples.LiveCaptions | head -n1 | cut -f4 | tr -d /" /")"
