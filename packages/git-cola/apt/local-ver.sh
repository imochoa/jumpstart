#!/usr/bin/env sh
# <<<AUTOGENERATED - DO NOT MODIFY>>>
#		 >     File: local-ver.sh
#		 >     Name: Git Cola
#		 > Template: apt

printf "git-cola > %s\n" "$(apt-cache policy git-cola | grep Installed | cut -d: -f2 | tr -d /" /")"
