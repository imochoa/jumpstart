#!/bin/bash
set -euo pipefail
IFS=$'\n\t'

# <<<AUTOGENERATED - DO NOT MODIFY>>>
#		 >     File: remove.sh
#		 >     Name: KeePassXC
#		 > Template: flatpak

flatpak uninstall org.keepassxc.KeePassXC  --delete-data
