# [[[cog
# ]]]
# [[[end]]]

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
