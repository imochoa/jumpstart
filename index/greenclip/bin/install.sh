#!/usr/bin/env bash

URL=$(curl --silent "https://api.github.com/repos/erebe/greenclip/releases/latest" \
  | jq -r '.assets[1].browser_download_url');

INSTALL_PATH="${HOME}/.local/bin/greenclip";

echo "Installing ${URL}";
curl ${URL} --location -o ${INSTALL_PATH};
sudo chmod +x ${INSTALL_PATH};
