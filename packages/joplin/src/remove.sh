#!/usr/bin/env bash

printf "Is this your home? %s" "${HOME}"
read -r

rm -r "${HOME}/.joplin"
rm -r "${HOME}/.config/joplin-desktop"
rm "${HOME}/.local/share/applications/appimagekit-joplin.desktop"
