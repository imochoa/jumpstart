#!/usr/bin/env bash

LAST_URL=$(curl -fsSLI -o /dev/null -w %{url_effective} https://github.com/nextcloud/desktop/releases/latest)
VER=$(echo ${LAST_URL} | cut -d/ -f8  | tr -d 'v')
BIN_DIR=${HOME}/.local/bin
DEST=${BIN_DIR}/nextcloud;

mkdir -p "${BIN_DIR}" \
&& /bin/rm -f "${DEST}" \
&& wget "https://github.com/nextcloud/desktop/releases/download/v${VER}/Nextcloud-${VER}-x86_64.AppImage" \
    --output-document="${DEST}" \
&& chmod +x "${DEST}";
