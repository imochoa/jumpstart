#!/usr/bin/env bash

INSTALL_DIR=/usr/local/share/fonts/nerdfonts
FONT_TEMPDIR=$(mktemp -d -t fonts-XXXXXXXXXX)

VER=$(git ls-remote --refs --tags https://github.com/ryanoasis/nerd-fonts \
    | cut --delimiter='/' --fields=3     \
    | tr '-' '~'                         \
    | sort --version-sort                \
    | tail --lines=1                     \
    | tr -d 'v'
    );

wget https://github.com/ryanoasis/nerd-fonts/archive/v${VER}.tar.gz \
  --continue                                                        \
  --output-document="${FONT_TEMPDIR}/nerdfonts.tar.gz"              \
&& tar xzf "${FONT_TEMPDIR}/nerdfonts.tar.gz"                       \
 --directory="${FONT_TEMPDIR}"                                      \
 --strip-components=1                                               \
&& sudo "${FONT_TEMPDIR}/install.sh" --install-to-system-path       \
&& fc-cache -f -v -r
# Regenerate the font cache

# System path requires sudo!
# sudo ./install.sh --install-to-system-path "Ubuntu"
# sudo ./install.sh --install-to-system-path "UbuntuMono"
# sudo ./install.sh --install-to-system-path "3270"
# sudo ./install.sh --install-to-system-path "FiraMono"
# sudo ./install.sh --install-to-system-path "FiraCode"
# sudo ./install.sh --install-to-system-path "SourceCodePro"
# sudo ./install.sh --install-to-system-path "RobotoMono"


# to test
# sudo ./install.sh --install-to-system-path "Hack Nerd Font"
