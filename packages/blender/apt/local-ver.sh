#!/bin/bash

# <<<AUTOGENERATED - DO NOT MODIFY>>>
#		 >     File: local-ver.sh
#		 >     Name: Blender
#		 > Template: apt

printf "blender > %s\n" "$(apt-cache policy blender | grep Installed | cut -d: -f2 | tr -d /" /")"
