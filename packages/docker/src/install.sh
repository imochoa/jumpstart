#!/usr/bin/env bash

# was also required?
# sudo apt install -y containerd

BASHCOMP=${BASHCOMP:-${HOME}/.config/bash/bash_completion}
ZSHCOMP=${ZSHCOMP:-${HOME}/.config/zsh/completions}

sudo apt install -y curl containerd \
&& sudo curl -sSL https://get.docker.com/ \
| sh && sudo usermod -aG docker ${USER}

sudo apt install docker.io
sudo systemctl enable --now docker
sudo usermod -aG docker ${USER}

echo "Getting autocompletion scripts"
DOCKERVER=$(docker version --format '{{.Server.Version}}' | sed 's/-.*//')
BASHURL=https://raw.githubusercontent.com/docker/cli/v${DOCKERVER}/contrib/completion/bash/docker
ZSHURL=https://raw.githubusercontent.com/docker/cli/v${DOCKERVER}/contrib/completion/zsh/_docker
mkdir -p "${BASHCOMP}"
mkdir -p "${ZSHCOMP}"
wget --output-document="${BASHCOMP}/docker"  "${BASHURL}"
wget --output-document="${ZSHCOMP}/_docker"  "${ZSHURL}"


#BASHURL=https://raw.githubusercontent.com/docker/cli/v$(docker version --format '{{.Server.Version}}' | sed 's/-.*//')/contrib/completion/bash/docker
#ZSHURL=https://raw.githubusercontent.com/docker/cli/v$(docker version --format '{{.Server.Version}}' | sed 's/-.*//')/contrib/completion/zsh/_docker



#https://github.com/docker/cli/blob/master/contrib/completion/zsh/_docker
#https://gist.github.com/toschneck/2df90c66e0f8d4c6567d69a36bfc5bcd
#https://github.com/Yelp/docker-compose/blob/master/docs/completion.md
