#!/bin/bash

# <<<AUTOGENERATED - DO NOT MODIFY>>>
#		 >     File: upstream-ver.sh
#		 >     Name: virtualbox
#		 > Template: apt

printf "virtualbox > %s\n" "$(apt-cache policy virtualbox | grep Candidate | cut -d: -f2 | tr -d /" /")"
printf "virtualbox-dkms > %s\n" "$(apt-cache policy virtualbox-dkms | grep Candidate | cut -d: -f2 | tr -d /" /")"
printf "virtualbox-ext-pack > %s\n" "$(apt-cache policy virtualbox-ext-pack | grep Candidate | cut -d: -f2 | tr -d /" /")"
printf "virtualbox-guest-dkms > %s\n" "$(apt-cache policy virtualbox-guest-dkms | grep Candidate | cut -d: -f2 | tr -d /" /")"
