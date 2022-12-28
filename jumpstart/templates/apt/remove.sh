# [[[cog
# import cog
# from cog_utils import str2list, HEADER, SH_SHEBANG
# cog.outl(f"{SH_SHEBANG}\n\n# {HEADER}")
# ]]]
# [[[end]]]

# [[[cog
# PPA_LIST=str2list(PPAS)
# if PPA_LIST:
#     cog.outl("sudo add-apt-repository --remove " + " ".join(PPA_LIST))
#
# PKG_LIST=str2list(PKGS)
# if not PKG_LIST:
#     raise ValueError()
# cog.outl("sudo apt-get remove -y " + " ".join(str2list(PKGS)))
# ]]]
# [[[end]]]
