#!/usr/bin/env sh
# <<<AUTOGENERATED - DO NOT MODIFY>>>
#		 > LOCAL-VER.SH
#		 > neovim
#		 > flatpak

printf "io.neovim.nvim > %s\n" "$(flatpak info io.neovim.nvim | grep Version | cut -d: -f2 | tr -d /" /")"