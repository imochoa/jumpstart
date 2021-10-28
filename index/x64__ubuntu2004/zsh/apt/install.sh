#!/usr/bin/env bash
sudo apt install -y zsh curl \
&& sudo apt install -y zsh-syntax-highlighting autojump \
&& sh -c "$(curl -fsSL https://raw.githubusercontent.com/zdharma/zinit/master/doc/install.sh)"
