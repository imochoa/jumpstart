#!/usr/bin/env bash
sudo apt install -y dunst
# Enable and configure it in systemd
systemctl restart --user dunst.service
