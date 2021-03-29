#!/usr/bin/env bash

sudo apt-get install -y software-properties-common \
&& sudo add-apt-repository -y ppa:kgilmer/speed-ricer \
&& sudo apt-get update -y \
&& sudo apt-get install -y i3-gaps i3-gaps-wm i3-snapshot arandr \
                        lxappearance rofi compton i3blocks xbacklight \
                        htop feh \
&& sudo apt-get install -y fonts-source-code-pro-ttf nordic moka-icon-theme
