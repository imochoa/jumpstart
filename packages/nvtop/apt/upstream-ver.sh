#!/bin/bash

# <<<AUTOGENERATED - DO NOT MODIFY>>>
#		 >     File: upstream-ver.sh
#		 >     Name: nvtop
#		 > Template: apt

printf "nvtop > %s\n" "$(apt-cache policy nvtop | grep Candidate | cut -d: -f2 | tr -d /" /")"
