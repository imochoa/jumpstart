#!/bin/bash
set -euo pipefail
IFS=$'\n\t'

# <<<AUTOGENERATED - DO NOT MODIFY>>>
#		 >     File: local-ver.sh
#		 >     Name: rich-cli
#		 > Template: pipx

pipx list | grep installed | grep rich-cli | ts -s ' ' | cut -d' ' -f8
