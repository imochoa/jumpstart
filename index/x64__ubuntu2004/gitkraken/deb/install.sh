#!/usr/bin/env bash


URL=https://release.gitkraken.com/linux/gitkraken-amd64.deb
TMP_DEB=/tmp/gitkraken-amd64.deb

sudo apt install -y wget \
  && wget ${URL} --output-document=${TMP_DEB} \
  && sudo apt install ${TMP_DEB}

# sudo dpkg -i ${TMP_DEB}
