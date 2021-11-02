#!/usr/bin/env sh

regolith-look set pop-os

# aptitude search i3xrocks* | grep '^i

# Just install the plugins you want
sudo apt install -y \
  i3xrocks                     	 \
  regolith-i3xrocks-config     	 \
  i3xrocks-battery             	 \
  i3xrocks-cpu-usage           	 \
  i3xrocks-rofication          	 \
  i3xrocks-todo                	 \
  i3xrocks-time

# Remove the others
sudo apt remove -y \
  i3xrocks-keyboard-layout     	 \
  i3xrocks-media-player        	 \
  i3xrocks-volume              	 \
  i3xrocks-info                	 \
  i3xrocks-bluetooth           	 \
  i3xrocks-openvpn             	 \
  i3xrocks-disk-capacity       	 \
  i3xrocks-key-indicator       	 \
  i3xrocks-nm-vpn              	 \
  i3xrocks-net-traffic         	 \
  i3xrocks-focused-window-name 	 \
  i3xrocks-wifi                	 \
  i3xrocks-app-launcher          \
  i3xrocks-next-workspace
