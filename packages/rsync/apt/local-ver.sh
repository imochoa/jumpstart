#!/bin/bash

# <<<AUTOGENERATED - DO NOT MODIFY>>>
#		 >     File: local-ver.sh
#		 >     Name: Rsync
#		 > Template: apt

printf "rsync > %s\n" "$(apt-cache policy rsync | grep Installed | cut -d: -f2 | tr -d /" /")"
