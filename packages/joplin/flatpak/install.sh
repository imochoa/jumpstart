#!/bin/bash
set -euo pipefail
IFS=$'\n\t'

# <<<AUTOGENERATED - DO NOT MODIFY>>>
#		 >     File: install.sh
#		 >     Name: Joplin
#		 > Template: flatpak

flatpak install -y flathub net.cozic.joplin_desktop
