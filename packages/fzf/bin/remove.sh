#!/usr/bin/env sh
# <<<AUTOGENERATED - DO NOT MODIFY>>>
#		 > REMOVE.SH
#		 > fzf
#		 > bin

# Variables
INSTALL_DST="${INSTALL_DST:-${HOME}/.local/bin/}"
BASHCOMP_P="${BASHCOMP_P:-${HOME}/.config/bash/bash_completion}"
ZSHCOMP="${ZSHCOMP:-${HOME}/.config/zsh/completions}"
TEMPDIR="$(mktemp -d -t XXXXXXXXXX)"
FMT='\e[0;34m%-6s\e[m\n'

# Commands
( [ -f "${INSTALL_DST}/fzf" ] && sudo rm "${INSTALL_DST}/fzf" || echo "${INSTALL_DST}/fzf does not exist" )
