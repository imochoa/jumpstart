#!/usr/bin/env bash
sudo apt install -y curl \
&& sudo curl -sSL https://get.docker.com/ \
| sh && sudo usermod -aG docker ${USER}

# sudo apt install docker.io
# sudo systemctl enable --now docker
# sudo usermod -aG docker ${USER}

echo "LOOK UP THE SHELL AUTOCOMPLETION HELPERS FOR DOCKER!";
