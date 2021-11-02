#!/usr/bin/env sh


VER=$(curl --silent "https://api.github.com/repos/sharkdp/fd/releases/latest" | jq ".tag_name")

echo "fd-find -> [${VER}]"
