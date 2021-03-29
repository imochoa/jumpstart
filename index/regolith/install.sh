#!/usr/bin/env bash
sudo apt install -y software-properties-common \
&& sudo add-apt-repository -y ppa:regolith-linux/release \
&& sudo apt update -y \
&& sudo apt install -y regolith-desktop-standard


#i3xrocks-battery
#sudo add-apt-repository ppa:regolith-linux/release \
#&& sudo apt-get update -y
#sudo apt install regolith-desktop-standard # or regolith-desktop-mobile for laptops