#!/usr/bin/env bash
# TODO FROM https://github.com/alacritty/alacritty/blob/master/INSTALL.md

sudo update-alternatives --remove-all alacritty

# Default?
# sudo gsettings set org.gnome.desktop.default-applications.terminal exec /usr/bin/alacritty
# sudo gsettings set org.gnome.desktop.default-applications.terminal exec-arg "-x"
sudo update-alternatives --remove-all alacritty || true
sudo update-alternatives --install /usr/bin/alacritty x-terminal-emulator /usr/local/bin/alacritty 100
# sudo update-alternatives --install /usr/local/bin/alacritty  x-terminal-emulator `realpath alacritty` 100
# https://blog.arranfrance.com/post/alacritty-and-byobu/
# apt-get install -y byobu
