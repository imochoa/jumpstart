#!/usr/bin/env sh

# <<<AUTOGENERATED FILE - DO NOT MODIFY>>>

printf "flameshot > %s\n" "$(apt-cache policy flameshot | grep Installed | cut -d: -f2 | tr -d /" /")"
