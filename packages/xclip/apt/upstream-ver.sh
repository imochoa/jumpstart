#!/bin/bash

# <<<AUTOGENERATED - DO NOT MODIFY>>>
#		 >     File: upstream-ver.sh
#		 >     Name: xclip
#		 > Template: apt

printf "xclip > %s\n" "$(apt-cache policy xclip | grep Candidate | cut -d: -f2 | tr -d /" /")"
