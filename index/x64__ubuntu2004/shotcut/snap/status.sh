#!/usr/bin/env sh
# AUTOGENERATED FILE! DO NOT MODIFY

missing=0;

    if $(snap list | cut -f1 -d' ' | tail -n +2 | grep -q 'shotcut' )
    then
       echo "[shotcut] -> [installed!]";
    else
       echo "[shotcut] -> [NOT installed!]";
       missing=1;
    fi
