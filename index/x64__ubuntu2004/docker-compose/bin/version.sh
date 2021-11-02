#!/usr/bin/env bash

VER=$(curl --silent "https://api.github.com/repos/docker/compose/releases/latest" \
  | jq ".tag_name" \
  | tr -d '"' )

echo "docker-compose -> [${VER}]"
