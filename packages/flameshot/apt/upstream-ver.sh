#!/bin/bash

# <<<AUTOGENERATED - DO NOT MODIFY>>>
#		 >     File: upstream-ver.sh
#		 >     Name: flameshot
#		 > Template: apt

printf "flameshot > %s\n" "$(apt-cache policy flameshot | grep Candidate | cut -d: -f2 | tr -d /" /")"
