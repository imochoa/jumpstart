#!/usr/bin/env bash

TMP_DEB=/tmp/google-chrome.deb

sudo apt install -y wget
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb --continue --output-document=${TMP_DEB}
sudo apt install ${TMP_DEB}
