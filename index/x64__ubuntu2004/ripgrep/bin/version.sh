#!/usr/bin/env sh


VER=$(curl --silent "https://api.github.com/repos/BurntSushi/ripgrep/releases/latest" | jq ".tag_name")

echo "ripgrep -> [${VER}]"
