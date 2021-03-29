#!/usr/bin/env bash
sudo add-apt-repository --remove ppa:linuxuprising/shutter \
&& sudo apt update -y \
&& sudo apt remove -y shutter
