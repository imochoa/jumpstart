#!/usr/bin/env sh
# AUTOGENERATED FILE! DO NOT MODIFY

# >>>> PPAS: regolith-linux/release
sudo apt-get install -y software-properties-common
sudo add-apt-repository -y ppa:regolith-linux/release
sudo apt-get update -y
# >>>> PKGS: i3xrocks i3xrocks-battery i3xrocks-cpu-usage i3xrocks-next-workspace i3xrocks-rofication i3xrocks-time i3xrocks-todo regolith-desktop-complete regolith-i3xrocks-config regolith-look-ubuntu
sudo apt-get install -y \
	i3xrocks \
	i3xrocks-battery \
	i3xrocks-cpu-usage \
	i3xrocks-next-workspace \
	i3xrocks-rofication \
	i3xrocks-time \
	i3xrocks-todo \
	regolith-desktop-standard \
	regolith-i3xrocks-config \
	regolith-look-ubuntu