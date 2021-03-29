#!/usr/bin/env bash
# Using Ubuntu
sudo apt-get install -y curl
curl -sL https://deb.nodesource.com/setup_lts.x | sudo -E bash -
sudo apt-get install -y nodejs

# update it
sudo npm install -g npm

# [OPTIONAL] To compile and install native addons from npm you may also need to install build tools:
sudo apt-get install -y build-essential
