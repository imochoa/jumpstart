#!/bin/bash

# <<<AUTOGENERATED - DO NOT MODIFY>>>
#		 >     File: upstream-ver.sh
#		 >     Name: Rsync
#		 > Template: apt

printf "rsync > %s\n" "$(apt-cache policy rsync | grep Candidate | cut -d: -f2 | tr -d /" /")"
