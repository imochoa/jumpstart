#!/bin/bash

# <<<AUTOGENERATED - DO NOT MODIFY>>>
#		 >     File: local-ver.sh
#		 >     Name: entr
#		 > Template: apt

printf "entr > %s\n" "$(apt-cache policy entr | grep Installed | cut -d: -f2 | tr -d /" /")"
