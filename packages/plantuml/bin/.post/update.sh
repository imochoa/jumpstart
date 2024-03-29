# [[[cog
# import cog
# from jumpstart.cogging.helpers import str2list, require_cmds, chain_cmds, printf
# from jumpstart.templates.bin.bin_cog_utils import install_bin
#
# ]]]
# [[[end]]]

VER=$(git ls-remote --refs --tags https://github.com/plantuml/plantuml |
      cut --delimiter='/' --fields=3 |
      grep -Eo 'v[0-9]+\.[0-9]+\.[0-9]+' |
      sort --version-sort |
      tr -d 'v' |
      tail --lines=1)
url="http://sourceforge.net/projects/plantuml/files/plantuml.${VER}.jar/download"

# Update .jar file?
# ----------------------------------------------------------------------------------
installdir="${HOME}/.local/share/plantuml"
# installdir="/usr/share/plantuml"
jarpath="${installdir}/plantuml.${VER}.jar"

mkdir -p ${installdir}
[ ! -f "${jarpath}" ] && curl -JLO --output "${jarpath}" "${url}"
ln -s -f "${installdir}/plantuml.${VER}.jar" "${installdir}/plantuml.jar"

# Update executable?
# ----------------------------------------------------------------------------------
wrapperpath="${HOME}/.local/bin/plantuml"
# wrapperpath="/usr/local/bin/plantuml"
DIR="$( cd -- "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"
echo $DIR
cp -f "${DIR}/run.sh" "${wrapperpath}"
