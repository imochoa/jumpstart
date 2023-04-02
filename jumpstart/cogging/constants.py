#!/usr/bin/env python3

"""
Only meant to be imported within cog
"""

# stdlib imports
from types import SimpleNamespace
import typing as T


class ENVVARS(SimpleNamespace):
    """
    OS Environment variables that are used in the templates
    INSTALLDIR=/usr/local/bin
    """

    INSTALL_DST: T.Final[str] = "INSTALL_DST"
    """
    INSTALLDIR = / usr / local / bin
    # Single-user
    INSTALLDIR = ~ /.local / bin /
    """
    FONT_P: T.Final[str] = "FONT_DST"
    """
    """
    WALLPAPER_P: T.Final[str] = "FONT_DST"
    """
    """
    BASHCOMP_P: T.Final[str] = "BASHCOMP_P"
    """
    =${BASHCOMP:-${HOME}/.config/bash/bash_completion}
    """
    ZSHCOMP_D: T.Final[str] = "ZSHCOMP_D"
    """
    =${ZSHCOMP:-${HOME}/.config/zsh/completions}
    """


class VARNAMES(SimpleNamespace):
    """
    Variable names to use in the shell scripts
    """

    TMPDIR = "DLTMP"
    """
    current temporary directory
    """
    DLFILE = "DLFILE"
    """
    Downloaded file (.tar.gz, .zip, ...)
    """
    DLPATH = "DLPATH"
    """
    full path of downloaded file
    """
    URL = "URL"
    """
    URL to download
    """
    SRCFILE = "SRCFILE"
    """
    """
    SRCPATH = "SRCPATH"
    """
    """
    DSTPATH = "SRCPATH"
    """
    """
    VERSION = "VER"
    """
    """


SH_SHEBANG: T.Final[str] = "#!/usr/bin/env sh"

HEADER: T.Final[str] = "<<<AUTOGENERATED FILE - DO NOT MODIFY>>>"
POST_HEADER: T.Final[str] = "<<<POST-AUTOGENERATED FILE - DO NOT MODIFY>>>"

PRINTF_FMT: T.Final[str] = r"\e[0;34m%-6s\e[m\n"

# TODO move envvars here?
# TODO replace rest
# TODO make a function for it?
SCRIPT_DEFAULTS: T.Final[str] = "\n".join(
    (
        f'{ENVVARS.INSTALL_DST}="${{{ENVVARS.INSTALL_DST}:-${{HOME}}/.local/bin/}}"',
        f'{ENVVARS.BASHCOMP_P}="${{{ENVVARS.BASHCOMP_P}:-${{HOME}}/.config/bash/bash_completion}}"',
        r'ZSHCOMP="${ZSHCOMP:-${HOME}/.config/zsh/completions}"',
        r'TEMPDIR="$(mktemp -d -t XXXXXXXXXX)"',
        r"FMT='\e[0;34m%-6s\e[m\n'",
    )
)


# echo "Global wallpapers at /usr/share/backgrounds"
# echo "Local wallpapers at ~/.local/share/backgrounds"
#
#
# BGDIR=/usr/share/backgrounds
# mkdir -p ${BGDIR}
# IMG_URL='https://unsplash.com/photos/VzRKG0piEp8/download?force=true'
# sudo wget ${IMG_URL} --continue --output-document=${BGDIR}/wallpaper.jpg
# sudo convert ${BGDIR}/wallpaper.jpg ${BGDIR}/wallpaper.png


class UserGlobalPath(T.NamedTuple):
    u: str
    """
    'USER' install
    """
    g: str
    """
    'GLOBAL' install
    """


class OSConfigPaths(T.NamedTuple):
    binaries: UserGlobalPath | None = None
    """
    """
    desktopfiles: UserGlobalPath | None = None
    """
    """
    icons: UserGlobalPath | None = None
    """
    """
    fonts: UserGlobalPath | None = None
    """
    """
    wallpapers: UserGlobalPath | None = None
    """
    """


class OSPaths(SimpleNamespace):
    """
    Variable names to use in the shell scripts
    """

    debian = OSConfigPaths(
        binaries=UserGlobalPath(
            u="${HOME}/.local/bin",
            g="/usr/local/bin",
        ),
        desktopfiles=UserGlobalPath(
            u="${HOME}/.local/share/applications",
            g="/usr/share/applications",
        ),
        icons=UserGlobalPath(
            u="${HOME}/.local/share/icons",
            g="/usr/share/icons",
            # /usr/share/pixmaps
            # /usr/share/icons
        ),
        fonts=UserGlobalPath(
            u="",
            g="/usr/local/share/fonts",
        ),
        wallpapers=UserGlobalPath(
            u="",
            g="/usr/share/backgrounds",
        ),
    )