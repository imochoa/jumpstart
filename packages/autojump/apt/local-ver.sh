#!/bin/bash

# <<<AUTOGENERATED - DO NOT MODIFY>>>
#		 >     File: local-ver.sh
#		 >     Name: autojump
#		 > Template: apt

printf "autojump > %s\n" "$(apt-cache policy autojump | grep Installed | cut -d: -f2 | tr -d /" /")"
