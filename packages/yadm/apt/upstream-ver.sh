#!/bin/bash

# <<<AUTOGENERATED - DO NOT MODIFY>>>
#		 >     File: upstream-ver.sh
#		 >     Name: yadm
#		 > Template: apt

printf "yadm > %s\n" "$(apt-cache policy yadm | grep Candidate | cut -d: -f2 | tr -d /" /")"
