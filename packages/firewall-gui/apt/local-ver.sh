#!/usr/bin/env sh
# <<<AUTOGENERATED - DO NOT MODIFY>>>
#		 >     File: local-ver.sh
#		 >     Name: firewall-gui
#		 > Template: apt

printf "gufw > %s\n" "$(apt-cache policy gufw | grep Installed | cut -d: -f2 | tr -d /" /")"
