#!/bin/bash
set -euo pipefail
IFS=$'\n\t'

# <<<AUTOGENERATED - DO NOT MODIFY>>>
#		 >     File: remove.sh
#		 >     Name: kooha
#		 > Template: flatpak

flatpak uninstall io.github.seadve.Kooha  --delete-data
