#!/usr/bin/env sh

# <<<AUTOGENERATED FILE - DO NOT MODIFY>>>

printf "baobab > %s\n" "$(apt-cache policy baobab | grep Installed | cut -d: -f2 | tr -d /" /")"
