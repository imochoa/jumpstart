#!/usr/bin/env sh
# <<<AUTOGENERATED - DO NOT MODIFY>>>
#		 >     File: local-ver.sh
#		 >     Name: ppa-purge
#		 > Template: apt

printf "ppa-purge > %s\n" "$(apt-cache policy ppa-purge | grep Installed | cut -d: -f2 | tr -d /" /")"
