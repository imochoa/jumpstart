#!/usr/bin/env sh

# <<<AUTOGENERATED FILE - DO NOT MODIFY>>>

printf "dconf-editor > %s\n" "$(apt-cache policy dconf-editor | grep Candidate | cut -d: -f2 | tr -d /" /")"
