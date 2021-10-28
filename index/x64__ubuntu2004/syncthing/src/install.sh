#!/usr/bin/env bash

sudo apt install curl apt-transport-https
curl -s https://syncthing.net/release-key.txt | sudo apt-key add
echo "deb https://apt.syncthing.net/ syncthing release" > /etc/apt/sources.list.d/syncthing.list
sudo apt-get update
sudo apt-get install syncthing
