#!/usr/bin/env sh

# DO NOT MODIFY!
# THIS FILE WAS AUTOGENERATED BY *generate-status-files.py*

missing=0;


if $(apt list --installed 'cookiecutter' | grep -q "\[installed\]")
then
   echo "[cookiecutter] -> [installed!]";
else
   echo "[cookiecutter] -> [NOT installed!]";
   missing=1;
fi


if [ "$missing" -eq "0" ];
then
    exit 0;
else
    exit 1;
fi
