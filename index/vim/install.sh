#!/usr/bin/env bash
sudo apt-get remove -y vim-tiny gvim \
&& sudo apt-get install -y vim vim-gtk \
&& vim +PluginInstall +qall
# Update!
