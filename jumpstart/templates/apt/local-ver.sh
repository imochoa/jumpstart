# [[[cog
# import cog
# from cog_utils import str2list, HEADER, SH_SHEBANG
# from apt_cog_utils import apt_local_ver_cmd
# cog.outl(f"{SH_SHEBANG}\n\n# {HEADER}")
# ]]]
# [[[end]]]

# [[[cog
# for pkg in str2list(PKGS):
#     cog.outl(apt_local_ver_cmd(pkg))
# ]]]
# [[[end]]]
