#!/usr/bin/env sh
# <<<AUTOGENERATED - DO NOT MODIFY>>>
#		 > UPSTREAM-VER.SH
#		 > imgcat
#		 > bin

# Commands
VER=$(curl -Ls -o /dev/null -w %{url_effective} https://github.com/danielgatis/imgcat/releases/latest | rev | cut -d/ -f1 | rev) \
    && printf "\e[0;34m%-6s\e[m\n" "imgcat > ${VER}\n"