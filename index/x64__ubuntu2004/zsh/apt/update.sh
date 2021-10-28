#!/usr/bin/env bash
cd "${HOME}/.zinit/bin" && git pull

# ZINIT!
# You can simple self upgrade zinit with the following command:
zinit self-update
# Also you can update all the plugins with:
zinit update



# AUTOCOMPLETION SCRIPTS!
COMPLETION_DIR="${HOME}/.config/zsh/completions"
wget https://raw.githubusercontent.com/cheat/cheat/master/scripts/cheat.zsh \
  --output-document="${COMPLETION_DIR}/_cheat.zsh"

wget https://raw.githubusercontent.com/docker/compose/master/contrib/completion/zsh/_docker-compose \
  --output-document="${COMPLETION_DIR}/_docker-compose.zsh"

wget https://github.com/docker/docker-ce/blob/master/components/cli/contrib/completion/zsh/_docker \
  --output-document="${COMPLETION_DIR}/_docker.zsh"

# todo? docker-goinside known-hosts?

wget https://raw.githubusercontent.com/BurntSushi/ripgrep/master/complete/_rg \
  --output-document="${COMPLETION_DIR}/_rg.zsh"

wget https://raw.githubusercontent.com/sharkdp/fd/master/contrib/completion/_fd \
  --output-document="${COMPLETION_DIR}/_fd.zsh"

# Standards: https://github.com/zsh-users/zsh/tree/zsh-5.8/Completion/Unix/Command
ZSHCOMPDIR="https://raw.githubusercontent.com/zsh-users/zsh/zsh-5.8/Completion/Unix/Command"
wget "${ZSHCOMPDIR}/_ssh" --output-document="${COMPLETION_DIR}/_ssh.zsh"
wget "${ZSHCOMPDIR}/_rsync" --output-document="${COMPLETION_DIR}/_rsync.zsh"
wget "${ZSHCOMPDIR}/_zip" --output-document="${COMPLETION_DIR}/_zip.zsh"
