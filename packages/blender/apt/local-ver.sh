#!/usr/bin/env sh

# <<<AUTOGENERATED FILE - DO NOT MODIFY>>>

printf "blender > %s\n" "$(apt-cache policy blender | grep Installed | cut -d: -f2 | tr -d /" /")"