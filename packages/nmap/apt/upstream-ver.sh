#!/usr/bin/env sh

# <<<AUTOGENERATED FILE - DO NOT MODIFY>>>

printf "nmap > %s\n" "$(apt-cache policy nmap | grep Candidate | cut -d: -f2 | tr -d /" /")"