#!/usr/bin/env bash

# >>>> PKGS: filemanager-actions nautilus-extension-gnome-terminal


# filemanager-actions: To configure nautilus
# nautilus-extension-gnome-terminal:  To start terminal at dir
sudo apt install -y filemanager-actions \
&& sudo apt install -y nautilus-extension-gnome-terminal

#nautilus-actions is outdated!
# Use filemanager-actions instead ( fma-config-tool  # To run the configuration tool )!
# https://askubuntu.com/questions/1288531/cant-open-nautilus-actions-in-ubuntu-20-04

# Run nautilus -q command to quit nautilus
# nautilus -q

# fma-config-tool  # To run the configuration tool
