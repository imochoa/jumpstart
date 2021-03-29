#!/usr/bin/env bash
sudo add-apt-repository --remove ppa:peek-developers/stable \
&& sudo apt-get update -y \
&& sudo apt remove -y peek
