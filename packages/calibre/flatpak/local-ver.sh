#!/usr/bin/env sh
# <<<AUTOGENERATED - DO NOT MODIFY>>>
#		 >     File: local-ver.sh
#		 >     Name: Calibre
#		 > Template: flatpak

printf "com.calibre_ebook.calibre > %s\n" "$(flatpak info com.calibre_ebook.calibre | grep Version | cut -d: -f2 | tr -d /" /")"
