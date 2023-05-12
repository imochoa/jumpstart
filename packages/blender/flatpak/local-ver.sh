#!/bin/bash
set -euo pipefail
IFS=$'\n\t'

# <<<AUTOGENERATED - DO NOT MODIFY>>>
#		 >     File: local-ver.sh
#		 >     Name: Blender
#		 > Template: flatpak

printf "org.blender.Blender > %s\n" "$(flatpak info org.blender.Blender | grep Version | cut -d: -f2 | tr -d /" /")"
