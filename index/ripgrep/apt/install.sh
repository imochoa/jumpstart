#!/usr/bin/env bash
sudo apt install -y ripgrep

# Fix for now...
echo "rg hould go before bat in 20.04 as discussed here: https://github.com/sharkdp/bat/issues/938"
sudo sed -i '/\/usr\/.crates2.json/d' /var/lib/dpkg/info/ripgrep.list
# ...