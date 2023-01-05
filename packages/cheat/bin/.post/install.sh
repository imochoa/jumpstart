# [[[cog
# import cog
# from cog_utils import str2list, require_cmds, chain_cmds, printf
# from bin_cog_utils import install_bin
#
# # Variables
#
# # For binary
# srcbin=r'"${TEMPDIR}/cheat"'
# dstbin=r'"${INSTALLDIR}/cheat"'
# cheat_gz=r'"${INSTALLDIR}/cheat.gz"'
#
# bashcomp_url=r"https://raw.githubusercontent.com/cheat/cheat/master/scripts/cheat.bash"
# zshcomp_url=r"https://raw.githubusercontent.com/cheat/cheat/master/scripts/cheat.zsh"
#
# # Requirements
# cog.outl(require_cmds(["curl", "wget", "jq", "gzip",]))
#
# # Commands
# cog.outl(install_bin(orgrepo=ORGREPO,filters=str2list(FILTERS)))
#
# cog.outl(chain_cmds((
# printf("Getting cheat"),
# r'wget "${URL}" --continue --output-document=' + cheat_gz,
# f"gzip -d {cheat_gz}",
# f"sudo chmod +x {cheat_gz}",
# f"sudo cp meow +x {cheat_gz}",
# "on",
# "you",
# )))
#
# ]]]
# [[[end]]]

echo "Downloading..." &&
  wget "${URL}" \
    --continue \
    --output-document="${TEMPDIR}/cheat.gz" &&
  echo "extracting..." &&
  gzip -d "${TEMPDIR}/cheat.gz" &&
  echo "Installing..." &&
  sudo chmod +x "${TEMPDIR}/cheat" &&
  sudo cp "${TEMPDIR}/cheat" "${INSTALLDIR}" &&
  echo "Copying autocomplete files..." &&
  mkdir -p "${BASHCOMP}" &&
  mkdir -p "${ZSHCOMP}" &&
  sudo wget --output-document="${BASHCOMP}/cheat.bash" https://raw.githubusercontent.com/cheat/cheat/master/scripts/cheat.bash &&
  sudo wget --output-document="${ZSHCOMP}/_cheat.zsh" https://raw.githubusercontent.com/cheat/cheat/master/scripts/cheat.zsh &&
  echo "installing the cheatsheets command" &&
  sudo wget --output-document="${INSTALLDIR}/cheatsheets" https://raw.githubusercontent.com/cheat/cheat/master/scripts/git/cheatsheets &&
  sudo chmod +x "${INSTALLDIR}/cheatsheets" &&
  mkdir -p ~/.config/cheat/cheatsheets/community &&
  mkdir -p ~/.config/cheat/cheatsheets/personal

# Get community cheasheets
git clone git@github.com:cheat/cheatsheets.git ~/.config/cheat/cheatsheets/community/
