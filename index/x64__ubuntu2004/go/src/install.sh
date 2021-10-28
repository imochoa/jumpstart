#!/usr/bin/env bash

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
# $ sudo wget -c http://geolite.maxmind.com/download/geoip/database/GeoLite2-Country.tar.gz -O - | sudo tar -xz -C /etc/nginx/
url="https://golang.org/dl/go1.17.linux-amd64.tar.gz"
sudo wget -c "${url}" -O - | sudo tar -xz -C /usr/local/ \
&& sudo ln -s /usr/local/go/bin/go /usr/local/bin \
&& sudo ln -s /usr/local/go/bin/gofmt /usr/local/bin

# sudo mkdir - /opt/go


# # UPDATED LINK!
# https://golang.org/dl/go1.17.linux-amd64.tar.gz

# sudo git clone https://github.com/golang/go.git /opt/go
