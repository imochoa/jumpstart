#!/usr/bin/env bash


INSTALLDIR=/usr/local/bin
BASHCOMP=${BASHCOMP:-${HOME}/.config/bash/bash_completion}
ZSHCOMP=${ZSHCOMP:-${HOME}/.config/zsh/completions}

sudo apt-get install -y curl wget jq

URL=$(curl --silent "https://api.github.com/repos/docker/compose/releases/latest" \
  | jq '..|.browser_download_url?' | grep -v 'sha256' | grep 'x86_64' | grep 'linux' \
  | tr -d '"' )

#sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o "${INSTALLDIR}/docker-compose"
sudo wget --output-document="${INSTALLDIR}/docker-compose" ${URL}
sudo chmod +x "${INSTALLDIR}/docker-compose"

# create the docker plugins directory if it doesn't exist yet
DOCKERPLUGINS=${HOME}/.docker/cli-plugins
mkdir -p "${DOCKERPLUGINS}"
# download the CLI into the plugins directory
curl -sSL "${URL}" -o "${DOCKERPLUGINS}/docker-compose"
# make the CLI executable
sudo chmod +x "${DOCKERPLUGINS}/docker-compose"

echo "Getting autocompletion scripts"
mkdir -p "${BASHCOMP}"
wget --output-document="${BASHCOMP}/docker-compose" https://raw.githubusercontent.com/docker/compose/$(docker-compose --version | awk 'NR==1{print $NF}')/contrib/completion/bash/docker-compose
mkdir -p "${ZSHCOMP}"
wget --output-document="${ZSHCOMP}/_docker-compose" https://raw.githubusercontent.com/docker/compose/$(docker-compose --version | awk 'NR==1{print $NF}')/contrib/completion/zsh/_docker-compose

#https://gist.github.com/toschneck/2df90c66e0f8d4c6567d69a36bfc5bcd
#https://github.com/Yelp/docker-compose/blob/master/docs/completion.md
