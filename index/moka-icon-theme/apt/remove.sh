#!/usr/bin/env bash
sudo add-apt-repository --remove ppa:snwh/ppa \
&& sudo apt remove -y moka-icon-theme faba-icon-theme faba-mono-icons \
&& sudo apt update
