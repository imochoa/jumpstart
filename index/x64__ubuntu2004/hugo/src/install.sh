#!/usr/bin/env bash

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

sudo mkdir -p /opt/hugo \
&& sudo git clone https://github.com/gohugoio/hugo.git /opt/hugo \
&& sudo chown -R $USER:$USER /opt/hugo \
&& cd /opt/hugo \
&& sudo go install --tags extended
