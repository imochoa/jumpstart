#!/usr/bin/env bash

echo "Global wallpapers at /usr/share/backgrounds"
echo "Local wallpapers at ~/.local/share/backgrounds"


BGDIR=/usr/share/backgrounds
mkdir -p ${BGDIR}
IMG_URL='https://unsplash.com/photos/VzRKG0piEp8/download?force=true'
sudo wget ${IMG_URL} --continue --output-document=${BGDIR}/wallpaper.jpg
sudo convert ${BGDIR}/wallpaper.jpg ${BGDIR}/wallpaper.png
