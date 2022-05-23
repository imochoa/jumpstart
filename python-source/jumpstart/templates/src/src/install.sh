#!/usr/bin/env bash

srcdir="/opt/goxel"
installdir="${HOME}/.local/bin"
# installdir="/usr/local/bin"

sudo apt install -y scons pkg-config libglfw3-dev libgtk-3-dev git \
&& ( [ -d /opt/goxel ] || sudo git clone https://github.com/guillaumechereau/goxel "${srcdir}" ) \
&& sudo chown -R ${USER}:${USER} "${srcdir}" \
&& cd "${srcdir}" \
&& git pull \
&& make release \
&& rm -f "${installdir}/goxel" \
&& sudo ln -s "${srcdir}/goxel" "${installdir}/goxel"
