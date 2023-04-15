#!/usr/bin/env sh


VER=$(curl --silent "https://api.github.com/repos/junegunn/fzf/releases/latest" | jq ".tag_name")

echo "fzf -> [${VER}]"
