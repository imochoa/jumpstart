#!/usr/bin/env bash
sudo apt-get install -y curl w3m jq
sudo wget https://raw.githubusercontent.com/sdushantha/tmpmail/master/tmpmail --continue --output-document=/usr/local/bin/tmpmail
sudo chown -R ${USER}:${USER} /usr/local/bin/tmpmail
sudo chmod +x /usr/local/bin/tmpmail
# Prepare first email
/usr/local/bin/tmpmail --generate
