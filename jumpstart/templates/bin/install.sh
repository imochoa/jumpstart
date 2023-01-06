# [[[cog
# import cog
# from cog_utils import str2list, HEADER, POST_HEADER, SH_SHEBANG, require_cmds, tempdir_cmd, SCRIPT_DEFAULTS, find_github_release
# from bin_cog_utils import install_bin
#
# cog.outl(f"{SH_SHEBANG}\n")
# cog.outl(f"# {HEADER}\n")
# cog.outl(f"# Variables\n{SCRIPT_DEFAULTS}\n")
#
# cog.outl(f"# Commands")
# github_release_cmd=find_github_release(orgrepo=ORGREPO,filters=str2list(FILTERS))
# if github_release_cmd:
#     cog.outl(f"GHRELEASEURL=\"$({github_release_cmd})\"\n")
#
# cog.outl(f"# {POST_HEADER}\n")
#
# ]]]
# [[[end]]]
