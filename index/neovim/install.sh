#!/usr/bin/env bash


# INSTALL NEOVIM 
VER=$(git ls-remote --refs --tags https://github.com/neovim/neovim |
  cut --delimiter='/' --fields=3 |
  tr '-' '~' |
  sort --version-sort |
  tail --lines=1)
# e.g. VER=v0.4.4

sudo rm -f /usr/local/bin/nvim \
&& sudo wget https://github.com/neovim/neovim/releases/download/${VER}/nvim.appimage --output-document=/usr/local/bin/nvim \
&& sudo chown ${USER}:${USER} /usr/local/bin/nvim \
&& sudo chmod +x /usr/local/bin/nvim \
&& sudo update-alternatives --install /usr/bin/nvim editor /usr/local/bin/nvim 100
# nvr expects "nvim" NOT "neovim"!

# SETUP
sudo apt install -y wget curl git xclip exuberant-ctags ncurses-term python3-pip python3-autopep8

# EXTRA DEPENDENCIES
# TODO DEPENDS ON NODEJS (install it as well)
# TODO for the fonts to look nice you need to install nerdfonts
# TODO FZF!
# mkdir -p ~/.config/nvim/pack/minpac/start/
# git clone --depth 1 https://github.com/junegunn/fzf.git ~/.config/nvim/pack/minpac/start/fzf
# ~/.config/nvim/pack/minpac/start/fzf/install

# PYTHON
sudo -H pip3 install --upgrade pip
sudo -H pip3 install --upgrade neovim pynvim flake8 jedi autopep8 neovim-remote

# NPM
# Update npm
sudo npm install -g npm
# nodejs Required by CoC
sudo npm install -g neovim
sudo npm install -g eslint

# BASIC NEOVIM SETUP
mkdir -p ~/.config/nvim \
&& touch ~/.config/nvim/init.vim \
mkdir -p ~/.config/nvim/pack/minpac/opt/minpac \
&& git clone https://github.com/k-takata/minpac.git ~/.config/nvim/pack/minpac/opt/minpac

# Config deps


# sudo apt install llvm and sudo apt-get install clang

# something like that...
# https://clangd.llvm.org/installation.html

# sudo apt-get installZQZQ clangd-9
# sudo update-alternatives --install /usr/bin/clangd clangd /usr/bin/clangd-9 100

# # Update!
# neovim +PackUpdate +qall
# neovim +CocInstall +qall
