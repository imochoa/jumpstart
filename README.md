# jumpstart

https://innovativeinnovation.github.io/ubuntu-setup/

top 100 security tools
https://sectools.org/

how to add a package

- dirname does not matter, metadata.json name does
- param name does not matter, params.json template does
- filenames must match. Same in .post & .pre

# TODO

- for apt, add "install-suggests"
  `sudo apt install clang --install-suggests`
  `sudo apt-get install libc++-dev `
- add .deb, bin, better define manual, snap
- docker tests?
- appimage belongs in bin
-
- for bin
  - how to find start/end filename?
  - chmod +x
  - move to install dir mv "name" "\${INSTALLDIR}/name?"

# Use a trap in case script exited

```
# Report on exit
# ----------------------------------------------------------------------------------------- #
trap 'notify-send --expire-time=10000 --app-name="wacom" "${PAD}" "${DESC_CONCAT}"' EXIT
```

# Packages to add

- poetry

```
# Installing poetry
curl -sSL https://install.python-poetry.org | python3 -

# Upgrade poetry
poetry self update
```

## Slow nautilus start

debug with:

```
 G_DEBUG="all" NAUTILUS_DEBUG="All" nautilus

 export G_DEBUG="all"
 export NAUTILUS_DEBUG="All"
 dbus-launch --exit-with-session nautilus
```

Is it samba share?
https://askubuntu.com/questions/1161928/nautilus-files-app-takes-long-time-to-start-on-ubuntu-18-04

Install net with sudo apt install samba-common-bin
then sudo mkdir -p /var/lib/samba/usershares/
and sudo chmod go+rwx /var/lib/samba/usershares/

apt-get purge xdg-desktop-portal-gtk

https://wiki.debian.org/Nautilus/FAQ/SlowNautilus

disable tracker?
https://askubuntu.com/questions/1385065/purging-performance-reducing-tracker-extract-caused-other-issues
https://askubuntu.com/questions/1187191/tracker-process-taking-lot-of-cpu/1187273#1187273

disable tracker with:
systemctl --user mask tracker-store.service tracker-miner-fs.service tracker-miner-rss.service tracker-extract.service tracker-miner-apps.service tracker-writeback.service
tracker reset --hard
sudo reboot

# Icons

https://itectec.com/ubuntu/ubuntu-where-are-the-desktop-icon-files-stored/

## Where to save .desktop files?

he .desktop link files are stored in /usr/share/applications for software installed for all users, and \$HOME/.local/share/applications for things you have installed only for yourself.

## Where to save .icon files? (Save as SVG!)

The actual icon (image) files are a bit more scattered (since a .desktop file can specify their absolute path), but /usr/share/pixmaps and /usr/share/icons contain a good fraction of them. (icons at $prefix/share/icons/ with required fall-back version in hicolor theme can be loaded without the full path, thus such as Icon=video-display where $prefix can be /usr, /usr/local or ~/.local; See specification at freedesktop.org: Icon Theme Specification )

sudo cp neovim-mark-flat.svg /usr/share/icons/neovim.svg

curl https://neovim.io/logos/neovim-logos.zip --output /tmp/logos.zip
unzip /tmp/logos.zip
sudo cp /tmp/neovim-mark-flat.svg /usr/share/icons/neovim.svg

sudo curl https://www.freecadweb.org/images/logo.png --output /usr/share/icons/freecad.png

# Extension

https://www.omgubuntu.co.uk/2022/02/clipboard-history-gnome-extension
https://github.com/MiSo1289/cmake-embed

https://github.com/shiftkey/desktop

# Use

jinja
rich
https://github.com/Textualize/rich

# PREFER .deb files!

sudo wget https://github.com/shiftkey/desktop/releases/download/release-2.9.3-linux3/GitHubDesktop-linux-2.9.3-linux3.deb

### Uncomment below line if you have not installed gdebi-core before

# sudo apt-get install gdebi-core

sudo gdebi GitHubDesktop-linux-2.9.3-linux3.deb

pix install jrnl

navi https://github.com/denisidoro/navi/releases/download/v2.19.0/navi-v2.19.0-x86_64-unknown-linux-musl.tar.gz

sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-key C99B11DEB97541F0
sudo apt-add-repository https://cli.github.com/packages
sudo apt update
sudo apt install gh

YAPPI!
https://coderzcolumn.com/tutorials/python/yappi-yet-another-python-profiler

# Docs yo

https://www.gitbook.com/explore

# default python version

update-alternatives --install /usr/bin/python python /usr/bin/python3 10

# MTP for phone on ubuntu

sudo apt-get install jmtpfs mtp-tools

# For nodejs/npm use nvm!

https://github.com/nvm-sh/nvm#installing-and-updating
nvm install --lts

with that, joplin CLI would be:
npm -g install joplin

# Joplin on CLI

command mode -> :
:help
:help all
:help keymap

1. run with no args to see options
   :config sync.target

2. choose your option (6: WebDAV)
   :config sync.target 6

3. Set sync params
   :config sync.6.path https://ewebdav.pcloud.com/joplin
   :config sync.6.username nachomartinochoa@gmail.com
   :config sync.6.password

:sync

:mkbook "notebook name!"
:mknote "note name!"

Android phones:
gvfs-fuse
