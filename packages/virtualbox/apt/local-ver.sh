#!/usr/bin/env sh
# <<<AUTOGENERATED - DO NOT MODIFY>>>
#		 > LOCAL-VER.SH
#		 > virtualbox
#		 > apt

printf "virtualbox > %s\n" "$(apt-cache policy virtualbox | grep Installed | cut -d: -f2 | tr -d /" /")"
printf "virtualbox-dkms > %s\n" "$(apt-cache policy virtualbox-dkms | grep Installed | cut -d: -f2 | tr -d /" /")"
printf "virtualbox-ext-pack > %s\n" "$(apt-cache policy virtualbox-ext-pack | grep Installed | cut -d: -f2 | tr -d /" /")"
printf "virtualbox-guest-dkms > %s\n" "$(apt-cache policy virtualbox-guest-dkms | grep Installed | cut -d: -f2 | tr -d /" /")"