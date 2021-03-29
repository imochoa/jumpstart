#!/usr/bin/env bash
sudo apt install -y python3 python3-pip python3-venv python3-dev  build-essential libssl-dev libffi-dev  libxml2-dev libxslt1-dev zlib1g-dev
# For python+PDF
sudo apt install -y texlive texlive-xetex texlive-latex-extra pandoc pandoc-citeproc
# For python+postgreSQL
sudo apt install -y libpq-dev python3-dev

# Upgrade pip
sudo -H pip3  install --upgrade pip
