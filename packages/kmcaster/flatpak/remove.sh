#!/bin/bash
set -euo pipefail
IFS=$'\n\t'

# <<<AUTOGENERATED - DO NOT MODIFY>>>
#		 >     File: remove.sh
#		 >     Name: KmCaster
#		 > Template: flatpak

flatpak uninstall com.whitemagicsoftware.kmcaster  --delete-data
