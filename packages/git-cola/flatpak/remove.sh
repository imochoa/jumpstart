#!/bin/bash
set -euo pipefail
IFS=$'\n\t'

# <<<AUTOGENERATED - DO NOT MODIFY>>>
#		 >     File: remove.sh
#		 >     Name: Git Cola
#		 > Template: flatpak

flatpak uninstall com.github.git_cola.git-cola  --delete-data
