#!/bin/bash
set -euo pipefail
IFS=$'\n\t'

# <<<AUTOGENERATED - DO NOT MODIFY>>>
#		 >     File: remove.sh
#		 >     Name: clamav
#		 > Template: apt

sudo apt-get remove -y clamav clamav-daemon
