#!/usr/bin/env bash
sudo apt install -y fonts-font-awesome fonts-noto-color-emoji
# Regenerate the font cache
fc-cache -f -v -r
