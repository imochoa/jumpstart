#!/usr/bin/env bash
# https://github.com/bootandy/dust/releases/download/v0.5.4/dust-v0.5.4-x86_64-unknown-linux-gnu.tar.gz

VER=$(git ls-remote --refs --tags https://github.com/bootandy/dust \
    | cut --delimiter='/' --fields=3     \
    | tr '-' '~'                         \
    | sort --version-sort                \
    | tail --lines=1);

URL="https://github.com/bootandy/dust/releases/download/${VER}/dust-${VER}-x86_64-unknown-linux-gnu.tar.gz";

INSTALL_PATH="${HOME}/.local/bin/dust";
INSTALL_TEMPDIR=$(mktemp -d -t dust-XXXXXXXXXX);
TMP_TARGZ="${INSTALL_TEMPDIR}/dust.tar.gz";

wget "${URL}"                                      \
  --continue                                       \
  --output-document=${TMP_TARGZ}                   \
&& tar xvzf ${TMP_TARGZ} -C ${INSTALL_TEMPDIR}     \
&& rm -f "${INSTALL_PATH}"                         \
&& cp ${INSTALL_TEMPDIR}/**/dust "${INSTALL_PATH}" \
&& sudo chmod +x ${INSTALL_PATH}
