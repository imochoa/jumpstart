#!/usr/bin/env sh

# <<<AUTOGENERATED FILE - DO NOT MODIFY>>>

printf "com.calibre_ebook.calibre > %s\n" "$(flatpak search com.calibre_ebook.calibre | head -n1 | cut -f4 | tr -d /" /")"