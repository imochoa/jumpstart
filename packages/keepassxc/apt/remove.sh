#!/bin/bash
set -euo pipefail
IFS=$'\n\t'

# <<<AUTOGENERATED - DO NOT MODIFY>>>
#		 >     File: remove.sh
#		 >     Name: KeePassXC
#		 > Template: apt

sudo add-apt-repository --remove ppa:phoerious/keepassxc
sudo apt-get remove -y keepassxc
