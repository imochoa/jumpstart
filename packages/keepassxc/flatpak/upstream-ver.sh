#!/bin/bash

# <<<AUTOGENERATED - DO NOT MODIFY>>>
#		 >     File: upstream-ver.sh
#		 >     Name: KeePassXC
#		 > Template: flatpak

printf "org.keepassxc.KeePassXC > %s\n" "$(flatpak search org.keepassxc.KeePassXC | head -n1 | cut -f4 | tr -d /" /")"
