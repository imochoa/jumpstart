#!/usr/bin/env sh
# <<<AUTOGENERATED - DO NOT MODIFY>>>
#		 >     File: local-ver.sh
#		 >     Name: graphviz
#		 > Template: apt

printf "graphviz > %s\n" "$(apt-cache policy graphviz | grep Installed | cut -d: -f2 | tr -d /" /")"
