# [[[cog
# import cog
# from cog_utils import str2list, HEADER, SH_SHEBANG
# from apt_cog_utils import add_pkgs, add_ppas
# cog.outl(f"{SH_SHEBANG}\n\n# {HEADER}")
# ]]]
# [[[end]]]

# [[[cog
# cog.outl(add_ppas(str2list(PPAS)))
# cog.outl(add_pkgs(str2list(PKGS)))
# ]]]
# [[[end]]]
