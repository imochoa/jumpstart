#!/usr/bin/env python3

"""
Only meant to be imported within cog
"""

# stdlib imports
from shlex import quote as sh_quote
import subprocess
import typing as T

# 3rd party imports
from cog_utils.cmds import chain_cmds, printf, require_cmds, tempdir_cmd
from cog_utils.constants import VARNAMES
from cog_utils.extractions import EXTRACTION_FCNS

# 1st party imports
from jumpstart.constants import ARCHIVE_EXTS, ENVVARS

# URL_CMD=url_cmd,
#             URL=self.cache.url,
#             ARCHIVE_EXT=self.cache.archive_ext,
#             VER_CMD=ver_cmd,


# # make tmpdir
# # Get URL
# release_url_cmd = find_github_release(orgrepo=orgrepo, filters=filters)
#
# # Extract
# release_url = subprocess.getoutput(release_url_cmd).replace('"', "").replace("'", "").lower()
# # Extract depending on extension
#
# passing_exts = [ext for ext in URLExts if release_url.endswith(ext)]
# if not passing_exts:
#     logger.error(ValueError(f"unknown extension: {release_url}"))
#     return ""
# ext = max(passing_exts, key=len)
# extraction_cmds = URLExts[ext]
#
# # Build command
# cmdlist = (
#         [
#             printf("downloading..."),
#             tempdir_cmd(VARNAMES.TMPDIR),
#             f'cd "${{{VARNAMES.TMPDIR}}}"',
#             # f'{VARNAMES.DLFILE}="dl{ext}"',
#             # f'{VARNAMES.DLPATH}="${{{VARNAMES.TMPDIR}}}/${{{VARNAMES.DLFILE}}}"',
#             f"{VARNAMES.URL}=$({release_url_cmd})",
#             f'curl -jLO "${VARNAMES.URL}"',
#             rf'{VARNAMES.DLFILE}="$(\ls . )"',
#             # f'{VARNAMES.DLPATH}="${{{VARNAMES.TMPDIR}}}/${{{VARNAMES.DLFILE}}}"',
#         ]
#         + extraction_cmds
#         + [
#             rf'{VARNAMES.SRCFILE}="$(\ls . )"',
#             f'sudo mv "${{{VARNAMES.SRCFILE}}}" ${{INSTALLDIR}}/{{CMDNAME}}',
#         ]
# )
#
# return chain_cmds(cmdlist)


def download_and_extract(
    url_cmd: str,
    archive_ext: str,
) -> list[str]:
    """ """
    exts_tuple: tuple[str, ...] = getattr(ARCHIVE_EXTS, archive_ext, tuple())

    cmds = [
        tempdir_cmd(VARNAMES.TMPDIR),
        f'cd "${{{VARNAMES.TMPDIR}}}"',
        printf(f"Downloading to $(realpath .)"),
        f"{VARNAMES.URL}=$({url_cmd})",
        f'curl -jLO "${{{VARNAMES.URL}}}"',
        f"{VARNAMES.DLFILE}=$(ls . | head -n1)",
    ]

    if exts_tuple:
        # TODO move extraction logs to the extraction fcns...
        cmds += (
            [
                printf(f"Extracting ${{{VARNAMES.DLFILE}}}"),
            ]
            + EXTRACTION_FCNS[exts_tuple](f"${{{VARNAMES.DLFILE}}}")
            + ['echo "$(ls .)"']
        )

    return cmds


if __name__ == "__main__":
    url_cmd = "curl --silent 'https://api.github.com/repos/cheat/cheat/releases/latest' | jq '..|.browser_download_url?' | grep 'linux' | grep 'amd64' | tr -d '\"'"
    print(chain_cmds(download_and_extract(url_cmd, archive_ext="GZ")))
    print("done!")
