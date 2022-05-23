echo "START"
echo ""
echo ""

VER=$(curl --silent "https://api.github.com/repos/FreeCAD/FreeCAD/releases/latest" \
  | jq ".tag_name" \
  | tr -d '"' )

echo $VER
RES=$(curl --silent "https://api.github.com/repos/FreeCAD/FreeCAD/releases/latest")

#TODO interactive Jq -> 
https://medium.com/@toja/parsing-github-releases-with-jq-13829c9ee82c


https://github.com/fiatjaf/jiq

or 
https://github.com/fiatjaf/ijq


echo $RES
# APPIMGDIR="/opt/AppImages"
# INSTALLDIR="/usr/local/bin"
# sudo apt-get install -y git

# # INSTALL NEOVIM
# VER=$(git ls-remote --refs --tags https://github.com/neovim/neovim |
#   cut --delimiter='/' --fields=3 |
#   tr '-' '~' |
#   sort --version-sort |
#   tail --lines=1)
# # e.g. VER=v0.4.4

# URL=https://github.com/neovim/neovim/releases/download/${VER}/nvim.appimage

# # nvr expects "nvim" NOT "neovim"!
# sudo rm -f "${INSTALLDIR}/nvim" \
#   && sudo wget ${URL} --output-document="${INSTALLDIR}/nvim" \
#   && sudo chown ${USER}:${USER} "${INSTALLDIR}/nvim" \
#   && sudo chmod +x "${INSTALLDIR}/nvim" \
#   && sudo update-alternatives --install /usr/bin/nvim editor "${INSTALLDIR}/nvim" 100

# # This last step might be more of a "setup" thing


echo ""
echo ""
echo ""
