#!/usr/bin/env sh

# <<<AUTOGENERATED FILE - DO NOT MODIFY>>>

printf "meld > %s\n" "$(apt-cache policy meld | grep Candidate | cut -d: -f2 | tr -d /" /")"