#!/usr/bin/env sh
# AUTOGENERATED FILE! DO NOT MODIFY

missing=0;

    if $(snap list | cut -f1 -d' ' | tail -n +2 | grep -q 'pycharm-professional' )
    then
       echo "[pycharm-professional] -> [installed!]";
    else
       echo "[pycharm-professional] -> [NOT installed!]";
       missing=1;
    fi