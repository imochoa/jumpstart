#!/bin/bash

# <<<AUTOGENERATED - DO NOT MODIFY>>>
#		 >     File: upstream-ver.sh
#		 >     Name: moreutils
#		 > Template: apt

printf "moreutils > %s\n" "$(apt-cache policy moreutils | grep Candidate | cut -d: -f2 | tr -d /" /")"
