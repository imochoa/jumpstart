#!/bin/bash

# <<<AUTOGENERATED - DO NOT MODIFY>>>
#		 >     File: local-ver.sh
#		 >     Name: clamav
#		 > Template: apt

printf "clamav > %s\n" "$(apt-cache policy clamav | grep Installed | cut -d: -f2 | tr -d /" /")"
printf "clamav-daemon > %s\n" "$(apt-cache policy clamav-daemon | grep Installed | cut -d: -f2 | tr -d /" /")"
