#!/usr/bin/env sh

# <<<AUTOGENERATED FILE - DO NOT MODIFY>>>

printf "redshift > %s\n" "$(apt-cache policy redshift | grep Installed | cut -d: -f2 | tr -d /" /")"
printf "redshift-gtk > %s\n" "$(apt-cache policy redshift-gtk | grep Installed | cut -d: -f2 | tr -d /" /")"
