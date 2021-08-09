#!/usr/bin/env bash

#Set as default screenshot tool:
#https://askubuntu.com/questions/1036473/ubuntu-18-how-to-change-screenshot-application-to-flameshot

gsettings set org.gnome.settings-daemon.plugins.media-keys screenshot '[]'
#Set a mapping of the "screenshot key" (PrtSc) to  /snap/bin/flameshot gui
