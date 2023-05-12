#!/bin/bash

# <<<AUTOGENERATED - DO NOT MODIFY>>>
#		 >     File: upstream-ver.sh
#		 >     Name: xxh
#		 > Template: pipx

VER=$(curl --silent -JL "https://pypi.org/project/xxh-xxh/" | grep --ignore-case --after-context=2 "release__version\"" | grep -v --ignore-case "class" | head -n1 | tr -s " ") \
&& printf "\e[0;34m%-6s\e[m\n" "[xxh-xxh] version was: ${VER}"
