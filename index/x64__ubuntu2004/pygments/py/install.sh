#!/usr/bin/env bash

VENVDIR="/opt/pyvenv"
sudo mkdir -p "${VENVDIR}"
# sudo python3 -m venv "${VENVDIR}"
sudo chown ${USER}:${USER} "${VENVDIR}"
sudo -H ${VENVDIR}/bin/python -m pip install Pygments

sudo ln -s /opt/pyvenv/bin/pygmentize /usr/local/bin/
sudo chmod +x /usr/local/bin/pygmentize
