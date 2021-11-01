#!/usr/bin/env bash
sudo apt install -y software-properties-common           \
&& sudo add-apt-repository -y ppa:regolith-linux/release \
&& sudo apt update -y                                    \
&& sudo apt install -y regolith-desktop-standard
# or regolith-desktop-mobile for laptops

# The following packages can be installed in place of regolith-desktop for specific sets of packages based on user needs: regolith-desktop-minimal, regolith-desktop-standard, regolith-desktop-mobile, and regolith-desktop-complete

# OPTIONAL
# Other Compositors?
# sudo apt install regolith-compositor-picom-glx # <--- DEFAULT
# sudo apt install regolith-compositor-none
# sudo apt install regolith-compositor-compton-glx
# sudo apt install regolith-compositor-xcompmgr

# PLUGINS
# Uninstall all of them
# apt-cache search i3xrocks | sed 's/ - .*//' - | xargs sudo apt remove -y

# Just install the plugins you want
sudo apt install -y \
  i3xrocks                     	 \
  i3xrocks-next-workspace      	 \
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
  i3xrocks-memory              	 \
  i3xrocks-disk-capacity       	 \
  i3xrocks-key-indicator       	 \
  i3xrocks-nm-vpn              	 \
  i3xrocks-net-traffic         	 \
  i3xrocks-focused-window-name 	 \
  i3xrocks-temp                	 \
  i3xrocks-wifi                	 \
  i3xrocks-weather

# See extra plugins: apt-cache search i3xrocks
# ❯ apt-cache search i3xrocks
# See installed plugins
# ❯ apt list --installed | grep i3xrocks

# i3xrocks - i3blocks with Xresources and conf.d configuration
# i3xrocks-battery - Indicator to show battery status.
# i3xrocks-bluetooth - Indicator to show currently connected Bluetooth devices.
# i3xrocks-cpu-usage - Indicator to show CPU load.
# i3xrocks-disk-capacity - Indicator for disk capacity.
# i3xrocks-focused-window-name - Indicator to show focused window name.
# i3xrocks-info - Indicator launch Remontoire.
# i3xrocks-key-indicator - Indicator for caps and num lock status.
# i3xrocks-keyboard-layout - Indicator to show keyboard layout.
# i3xrocks-media-player - Indicator for managing media playback.
# i3xrocks-memory - Indicator to show memory utilization.
# i3xrocks-net-traffic - Indicator to show network I/O status.
# i3xrocks-next-workspace - Button to open next workspace.
# i3xrocks-nm-vpn - Network-Manager VPN indicator.
# i3xrocks-openvpn - Indicator to show openvpn status.
# i3xrocks-rofication - Status indicator for rofication
# i3xrocks-temp - Indicator for system temperature.
# i3xrocks-time - Indicator to show date and time.
# i3xrocks-todo - Indicator to mange and show to-do list.
# i3xrocks-volume - Indicator to show volume.
# i3xrocks-weather - Indicator to show local weather.
# i3xrocks-wifi - Indicator to display the current Wi-Fi network name.
# regolith-i3xrocks-config - Regolith configuration for i3xrocks launcher
# regolith-todo - A to-do blocklet for i3xrocks OUTDATED -> i3xrocks-todo?


# THEMES?
# sudo apt install regolith-look-ubuntu
