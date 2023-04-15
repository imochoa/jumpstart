#!/usr/bin/env bash

VER=$(curl --silent "https://api.github.com/repos/aristocratos/btop/releases/latest" \
      | jq '.tag_name' | tr -d '"')
echo $VER
