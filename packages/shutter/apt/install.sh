#!/bin/bash
set -euo pipefail
IFS=$'\n\t'

# <<<AUTOGENERATED - DO NOT MODIFY>>>
#		 >     File: install.sh
#		 >     Name: Shutter
#		 > Template: apt

sudo add-apt-repository -y universe
sudo apt-get update -y
sudo apt-get install -y shutter
