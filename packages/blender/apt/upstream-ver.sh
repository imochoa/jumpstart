#!/usr/bin/env sh
# <<<AUTOGENERATED - DO NOT MODIFY>>>
#		 >     File: upstream-ver.sh
#		 >     Name: Blender
#		 > Template: apt

printf "blender > %s\n" "$(apt-cache policy blender | grep Candidate | cut -d: -f2 | tr -d /" /")"
