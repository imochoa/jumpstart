#!/bin/bash
set -euo pipefail
IFS=$'\n\t'

# <<<AUTOGENERATED - DO NOT MODIFY>>>
#		 >     File: upstream-ver.sh
#		 >     Name: Calibre
#		 > Template: flatpak

printf "com.calibre_ebook.calibre > %s\n" "$(flatpak search com.calibre_ebook.calibre | head -n1 | cut -f4 | tr -d /" /")"
