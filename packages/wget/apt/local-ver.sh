#!/usr/bin/env sh

# <<<AUTOGENERATED FILE - DO NOT MODIFY>>>

printf "wget > %s\n" "$(apt-cache policy wget | grep Installed | cut -d: -f2 | tr -d /" /")"
