#!/bin/bash
set -euo pipefail
IFS=$'\n\t'

# <<<AUTOGENERATED - DO NOT MODIFY>>>
#		 >     File: remove.sh
#		 >     Name: lua
#		 > Template: apt

sudo apt-get remove -y lua5.3 luarocks luajit
