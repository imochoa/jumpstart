#!/bin/bash

# <<<AUTOGENERATED - DO NOT MODIFY>>>
#		 >     File: upstream-ver.sh
#		 >     Name: suckless-tools
#		 > Template: apt

printf "suckless-tools > %s\n" "$(apt-cache policy suckless-tools | grep Candidate | cut -d: -f2 | tr -d /" /")"
