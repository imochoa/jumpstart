#!/usr/bin/env sh

# <<<AUTOGENERATED FILE - DO NOT MODIFY>>>

printf "arandr > %s\n" "$(apt-cache policy arandr | grep Installed | cut -d: -f2 | tr -d /" /")"