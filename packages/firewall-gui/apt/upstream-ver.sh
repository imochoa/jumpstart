#!/usr/bin/env sh

# <<<AUTOGENERATED FILE - DO NOT MODIFY>>>

printf "gufw > %s\n" "$(apt-cache policy gufw | grep Candidate | cut -d: -f2 | tr -d /" /")"
