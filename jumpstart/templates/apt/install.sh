# [[[cog
# import cog
# from cog_utils import str2list, HEADER, SH_SHEBANG
# cog.outl(f"{SH_SHEBANG}\n\n# {HEADER}")
# ]]]
# [[[end]]]

# [[[cog
# PPA_LIST=str2list(PPAS)
# if PPA_LIST:
#     cog.outl("sudo add-apt-repository -y" + " ".join(PPA_LIST))
#     cog.outl("sudo apt-get update -y")
#
# PKG_LIST=str2list(PKGS)
# if not PKG_LIST:
#     raise ValueError()
# cog.outl("sudo apt-get install -y " + " ".join(str2list(PKGS)))
# ]]]
# [[[end]]]
