#!/usr/bin/env sh

# <<<AUTOGENERATED FILE - DO NOT MODIFY>>>

printf "dunst > %s\n" "$(apt-cache policy dunst | grep Candidate | cut -d: -f2 | tr -d /" /")"
