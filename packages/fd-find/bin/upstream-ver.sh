#!/usr/bin/env sh
# <<<AUTOGENERATED - DO NOT MODIFY>>>
#		 > UPSTREAM-VER.SH
#		 > fd-find
#		 > bin

# Commands
VER=$(curl -Ls -o /dev/null -w %{url_effective} https://github.com/junegunn/fzf/releases/latest | rev | cut -d/ -f1 | rev) \
    && printf "\e[0;34m%-6s\e[m\n" "fd-find > ${VER}\n"