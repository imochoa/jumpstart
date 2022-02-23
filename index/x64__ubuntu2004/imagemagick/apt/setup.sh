#!/usr/bin/env sh

# https://stackoverflow.com/questions/52998331/imagemagick-security-policy-pdf-blocking-conversion
# TODD ONLY SAFE IF ghostscript version is over: 9.26


for f in /etc/ImageMagick-*/policy.xml
do
    [ ! -f "$f.back" ] && { echo -e "Making a backup at $f -> $f.back"; sudo cp "$f" "$f.back"; };
    # sudo cp "$f" "$f.back";
    sudo sed -i '/disable ghostscript format types/,+6d' "$f"
done
