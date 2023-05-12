#!/bin/bash
set -euo pipefail
IFS=$'\n\t'

# <<<AUTOGENERATED - DO NOT MODIFY>>>
#		 >     File: local-ver.sh
#		 >     Name: trash-cli
#		 > Template: pipx

pipx list | grep installed | grep trash-cli | ts -s ' ' | cut -d' ' -f8
