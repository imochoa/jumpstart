#!/usr/bin/env sh

# <<<AUTOGENERATED FILE - DO NOT MODIFY>>>

printf "dos2unix > %s\n" "$(apt-cache policy dos2unix | grep Installed | cut -d: -f2 | tr -d /" /")"