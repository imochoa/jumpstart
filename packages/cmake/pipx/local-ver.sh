#!/usr/bin/env sh
# <<<AUTOGENERATED - DO NOT MODIFY>>>
#		 >     File: local-ver.sh
#		 >     Name: CMake
#		 > Template: pipx

pipx list | grep installed | grep cmake | ts -s ' ' | cut -d' ' -f8
