#!/usr/bin/env sh
# <<<AUTOGENERATED - DO NOT MODIFY>>>
#		 > UPSTREAM-VER.SH
#		 > openVPN
#		 > apt

printf "easy-rsa > %s\n" "$(apt-cache policy easy-rsa | grep Candidate | cut -d: -f2 | tr -d /" /")"
printf "network-manager-openvpn > %s\n" "$(apt-cache policy network-manager-openvpn | grep Candidate | cut -d: -f2 | tr -d /" /")"
printf "openvpn > %s\n" "$(apt-cache policy openvpn | grep Candidate | cut -d: -f2 | tr -d /" /")"