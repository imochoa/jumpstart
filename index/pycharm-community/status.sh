#!/usr/bin/env sh
missing=0;

if $(snap list | cut -f1 -d' ' | tail -n +2 | grep -q 'pycharm-community')
then
   echo "[pycharm-community] -> [installed!]";
else
   echo "[pycharm-community] -> [NOT installed!]";
   exit 1;
fi


if [ "$missing" -eq "0" ];
then
    exit 0;
else
    exit 1;
fi

