#!/usr/bin/env bash

# sudo apt install docker.io
# sudo systemctl enable --now docker
# sudo usermod -aG docker ${USER}

# Use buildkit enhancements by default
# https://docs.docker.com/develop/develop-images/build_enhancements/
APT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
CONFIG_JSON=$(realpath "${APT_DIR}/../files/daemon.json")


if [ -f "${CONFIG_JSON}" ]; then

  sudo cp "${CONFIG_JSON}" /etc/docker/daemon.json
  # For snap install?
  # /var/snap/docker/current/config

  echo "Copied docker/daemon.json"
else
  echo "Could not find ${CONFIG_JSON}!"
  echo "Skipping docker/daemon.json config!"
fi
