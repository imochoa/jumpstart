#!/usr/bin/env sh
# <<<AUTOGENERATED - DO NOT MODIFY>>>
#		 >     File: upstream-ver.sh
#		 >     Name: Git Cola
#		 > Template: pipx

VER=$(curl --silent -JL "https://pypi.org/project/git-cola/" | grep --ignore-case --after-context=2 "release__version\"" | grep -v --ignore-case "class" | head -n1 | tr -s " ") \
&& printf "\e[0;34m%-6s\e[m\n" "[git-cola] version was: ${VER}"