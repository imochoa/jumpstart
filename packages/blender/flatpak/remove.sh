#!/bin/bash
set -euo pipefail
IFS=$'\n\t'

# <<<AUTOGENERATED - DO NOT MODIFY>>>
#		 >     File: remove.sh
#		 >     Name: Blender
#		 > Template: flatpak

flatpak uninstall org.blender.Blender  --delete-data
