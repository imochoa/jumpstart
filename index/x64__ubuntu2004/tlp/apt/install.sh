#!/usr/bin/env sh
# AUTOGENERATED FILE! DO NOT MODIFY

# >>>> PPAS: linuxuprising/apps
sudo apt-get install -y software-properties-common
sudo add-apt-repository -y ppa:linuxuprising/apps
sudo apt-get update -y
# >>>> PKGS: tlp tlp-rdw tlpui
sudo apt-get install -y \
	tlp \
	tlp-rdw \
	tlpui
