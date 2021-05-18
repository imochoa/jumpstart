#!/usr/bin/env python3
import ipdb
import re
import os
import stat
import typing as T

# import enum
import pathlib

from jumpstart import INDEX_DIR, AppFilenames

# Specific


# class InstallTypes(enum.Enum):
#     apt = r"apt\s+install"
#     snap = r"snap\s+install"


def load_script(p: pathlib.Path):
    comment_m = "#"

    with open(p, "r") as fp:
        lines = fp.readlines()

    # lines = (l for l in lines if not l.startswith(comment_m))
    lines = (l[: l.find(comment_m)] for l in lines)
    lines = (l.strip() for l in lines)
    lines = (l if l else ";" for l in lines)
    txt = "\n".join(lines)

    txt = re.sub(
        pattern=r"\s*\\\n\s*",
        repl=" ",
        string=txt,
    )

    txt = re.sub(
        pattern=r"\s+",
        repl=" ",
        string=txt,
    )

    # txt = re.sub(
    #     pattern=r";\s+;",
    #     repl=";",
    #     string=txt,
    # )

    return txt


class Votes(T.NamedTuple):
    apt: T.List[str] = []
    snap: T.List[str] = []
    curl: T.List[str] = []
    wget: T.List[str] = []


def apt_pkgs(txt: str) -> T.List[str]:
    # (?P<pkgs>(?:\s[a-zA-Z0-9-_]+)+)\s*(;|\n)
    # if 'p7zip' in txt:
    m = re.search(
        pattern=r"apt(?:-get)?\s+install(?:\s+-y)?(?P<pkgs>(?:\s[a-zA-Z0-9-_]+)+)\s*(;|\n|\b)",
        string=txt,
        # flags=re.MULTILINE,
    )

    if not m:
        return []

    return [p for p in m.groupdict().get("pkgs", "").split()]


def snap_pkgs(txt: str) -> T.List[str]:
    m = re.search(
        # pattern=r"apt(?:-get)?\s+install(?:\s+-y)?(?P<pkgs>(?:\s+\S+)+)",
        pattern=r"snap\s+install(?:\s+-{1,2}\w+)*(?P<pkgs>(?:\s[a-zA-Z0-9-_]+)+)\s*(;|\n|\b)",
        string=txt,
        # flags=re.MULTILINE,
    )

    if not m:
        return []
    return [p for p in m.groupdict().get("pkgs", "").split()]


def check_app(d: pathlib.Path) -> Votes:

    install_script = [
        f for f in d.iterdir() if f.name.startswith(AppFilenames.install.value)
    ]

    if not install_script:
        print(f"No install script in {d}")
        return Votes()
    elif len(install_script) > 1:
        print(f"Too many install scripts in {d}!")

    txt = load_script(install_script[0])
    # kwargs = {f: False for f in Votes._fields}
    # with open(install_script[0], "r") as fp:
    #     txt = fp.read()

    v = Votes(
        apt=apt_pkgs(txt),
        snap=snap_pkgs(txt),
    )

    # print(v, txt)

    return v


def apt_status(pgks: T.List[str]) -> str:

    sh_txt = """#!/usr/bin/env sh
missing=0;

"""

    for pkg in pgks:
        sh_txt += f"""
if $(apt list --installed '{pkg}' | grep -q "\\[installed\\]")
then
   echo "[{pkg}] -> [installed!]";
else
   echo "[{pkg}] -> [NOT installed!]";
   missing=1;
fi

"""
    sh_txt += """
if [ "$missing" -eq "0" ];
then
    exit 0;
else
    exit 1;
fi


"""

    return sh_txt


def snap_status(pgks: T.List[str]) -> str:
    sh_txt = """#!/usr/bin/env sh
missing=0;
"""

    # snap list | cut -f1 -d' ' | tail -n +2 | grep 'spotify'
    for pkg in pgks:

        sh_txt += f"""
if $(snap list | cut -f1 -d' ' | tail -n +2 | grep -q '{pkg}')
then
   echo "[{pkg}] -> [installed!]";
else
   echo "[{pkg}] -> [NOT installed!]";
   exit 1;
fi

"""

    sh_txt += """
if [ "$missing" -eq "0" ];
then
    exit 0;
else
    exit 1;
fi

"""
    return sh_txt


if __name__ == "__main__":

    unknown_install_types = []
    for d in (p for p in INDEX_DIR.iterdir() if p.is_dir()):
        v = check_app(d)
        k_matches = [k for k, v in v._asdict().items() if v]
        match_count = len(k_matches)
        if match_count == 0:
            print(f"Unkown install type for {d}")
            unknown_install_types.append(d)
            continue
        elif match_count > 1:
            print(f"Too many install types for {d}")
            unknown_install_types.append(d)
            continue
        k = k_matches[0]
        pkgs = getattr(v, k)

        print(f"Just one install type: {k} -> {pkgs}")

        fcn = {
            "apt": apt_status,
            "snap": snap_status,
        }.get(k)
        if fcn is None:
            print(f"No fcn for {k}!")
            continue

        # with open
        status_f = d / f"{AppFilenames.status.value}.sh"
        with open(status_f, "w") as fp:
            fp.write(fcn(pkgs))

        st = status_f.stat()
        status_f.chmod(st.st_mode | stat.S_IEXEC)
        print(f"Wrote {status_f} {st.st_size/1e3:.1f} [Kb]")

    if unknown_install_types:
        unknown_report = "\n\t> ".join(
            [f"\n[{len(unknown_install_types)}] Non-auto status scripts\n"]
            + [f.name for f in unknown_install_types]
        )
        print(unknown_report)
