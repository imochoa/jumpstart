#!/usr/bin/env bash
# https://github.com/docker/compose/releases
VER=1.26.2
sudo apt-get install -y curl \
&& sudo curl -L https://github.com/docker/compose/releases/download/${VER}/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose \
&& sudo chmod +x /usr/local/bin/docker-compose
