#!/usr/bin/env sh

# <<<AUTOGENERATED FILE - DO NOT MODIFY>>>

printf "yadm > %s\n" "$(apt-cache policy yadm | grep Installed | cut -d: -f2 | tr -d /" /")"