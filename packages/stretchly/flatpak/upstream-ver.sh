#!/usr/bin/env sh
# <<<AUTOGENERATED - DO NOT MODIFY>>>
#		 > UPSTREAM-VER.SH
#		 > stretchly
#		 > flatpak

printf "net.hovancik.Stretchly > %s\n" "$(flatpak search net.hovancik.Stretchly | head -n1 | cut -f4 | tr -d /" /")"
