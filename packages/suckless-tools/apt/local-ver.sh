#!/usr/bin/env sh

# <<<AUTOGENERATED FILE - DO NOT MODIFY>>>

printf "suckless-tools > %s\n" "$(apt-cache policy suckless-tools | grep Installed | cut -d: -f2 | tr -d /" /")"
