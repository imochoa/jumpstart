#!/usr/bin/env sh

# <<<AUTOGENERATED FILE - DO NOT MODIFY>>>

printf "tree > %s\n" "$(apt-cache policy tree | grep Candidate | cut -d: -f2 | tr -d /" /")"