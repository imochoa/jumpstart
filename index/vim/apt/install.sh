#!/usr/bin/env bash
sudo apt remove -y vim-tiny gvim \
&& sudo apt install -y vim vim-gtk \
&& vim +PluginInstall +qall
# Update!
