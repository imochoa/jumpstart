#!/bin/bash
set -euo pipefail
IFS=$'\n\t'

# <<<AUTOGENERATED - DO NOT MODIFY>>>
#		 >     File: install.sh
#		 >     Name: yadm
#		 > Template: apt

sudo apt-get install -y yadm

# Useful since there are tons of untracked files
yadm gitconfig gui.displayuntracked false
Warning: no cog code found in /home/imochoa/Code/jumpstart/packages/yadm/apt/.post/install.sh
