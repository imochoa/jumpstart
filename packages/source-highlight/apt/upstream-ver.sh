#!/usr/bin/env sh

# <<<AUTOGENERATED FILE - DO NOT MODIFY>>>

printf "source-highlight > %s\n" "$(apt-cache policy source-highlight | grep Candidate | cut -d: -f2 | tr -d /" /")"