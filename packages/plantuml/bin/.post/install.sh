# [[[cog
# import cog
# from jumpstart.cogging.helpers import str2list, require_cmds, chain_cmds, printf
# from jumpstart.templates.bin.bin_cog_utils import install_bin
#
# ]]]
# [[[end]]]

# TODO use INSTALL_DST?
installdir="${HOME}/.local/share/plantuml"
# installdir="/usr/share/plantuml"
jarpath="${installdir}/plantuml.jar"
mkdir -p ${installdir}
mv *.jar "${jarpath}"
# ln -s -f "${installdir}/plantuml.${VER}.jar" "${installdir}/plantuml.jar"

# Update executable?
# ----------------------------------------------------------------------------------
# CONSTANTS
DATA_DIR="/home/imochoa/Code/jumpstart/packages/plantuml/bin/data/"
RUN_WRAPPER="${DATA_DIR}/plantuml"

wrapperpath="${HOME}/.local/bin/plantuml"
# wrapperpath="/usr/local/bin/plantuml"
DIR="$(
	cd -- "$(dirname "$0")" >/dev/null 2>&1
	pwd -P
)"
echo $DIR
# cp -f "${DIR}/run.sh" "${wrapperpath}"
cp -f "${RUN_WRAPPER}" "${wrapperpath}"
