#!/usr/bin/env sh

# <<<AUTOGENERATED FILE - DO NOT MODIFY>>>

printf "sxiv > %s\n" "$(apt-cache policy sxiv | grep Installed | cut -d: -f2 | tr -d /" /")"
