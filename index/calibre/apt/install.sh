#!/usr/bin/env bash
sudo apt install -y wget \
&& sudo -v \
&& wget -nv -O- https://download.calibre-ebook.com/linux-installer.sh \
| sudo sh /dev/stdin