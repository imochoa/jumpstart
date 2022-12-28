# [[[cog
# import cog
# from cog_utils import str2list, HEADER, SH_SHEBANG
# from apt_cog_utils import remove_pkgs, remove_ppas
# cog.outl(f"{SH_SHEBANG}\n\n# {HEADER}")
# ]]]
# [[[end]]]

# [[[cog
# cog.outl(remove_ppas(str2list(PPAS)))
# cog.outl(remove_pkgs(str2list(PKGS)))
# ]]]
# [[[end]]]
