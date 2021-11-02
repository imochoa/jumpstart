#!/usr/bin/env sh

VER=$(curl --silent "https://api.github.com/repos/sharkdp/bat/releases/latest" \
  | jq ".tag_name" \
  | tr -d '"' )

echo "bat -> [${VER}]"
