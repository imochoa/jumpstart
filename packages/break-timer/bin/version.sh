#!/usr/bin/env sh

# TODO!
VER=$(curl --silent "https://api.github.com/repos/sharkdp/bat/releases/latest" \
  | jq ".tag_name" \
  | tr -d '"' )

echo "bat -> [${VER}]"
