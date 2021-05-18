#!/usr/bin/env sh
missing=0;


if $(apt list --installed 'tmux' | grep -q "\[installed\]")
then
   echo "[tmux] -> [installed!]";
else
   echo "[tmux] -> [NOT installed!]";
   missing=1;
fi


if [ "$missing" -eq "0" ];
then
    exit 0;
else
    exit 1;
fi


