#!/usr/bin/env bash

# VENVDIR=${HOME}/.virtualenvs/trash-cli
VENVDIR="/opt/pyvenv"
# INSTALLDIR=${HOME}/.local/bin
INSTALLDIR=/usr/local/bin


##!/usr/bin/env bash

#VENVDIR="/opt/pyvenv"
#sudo mkdir -p "${VENVDIR}"
## sudo python3 -m venv "${VENVDIR}"
#sudo chown ${USER}:${USER} "${VENVDIR}"
#sudo -H ${VENVDIR}/bin/python -m pip install Pygments

#sudo ln -s /opt/pyvenv/bin/pygmentize /usr/local/bin/
#sudo chmod +x /usr/local/bin/pygmentize

sudo -H missing from pip install

mkdir -p "${VENVDIR}"                                            \
  && python -m venv "${VENVDIR}"                                 \
  && "${VENVDIR}/bin/pip" install --upgrade pip setuptools wheel \
  && sudo -H "${VENVDIR}/bin/pip" install --upgrade trash-cli \
  && sudo ln -s ${VENVDIR}/bin/trash* "${INSTALLDIR}"


sudo chmod +x /usr/local/bin/trash*
