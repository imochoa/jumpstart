#!/usr/bin/env sh
# AUTOGENERATED FILE! DO NOT MODIFY

missing=0;

if $(apt list --installed 'dunst' | grep -q "\[installed\]")
then
   echo "[dunst] -> [installed!]";
else
   echo "[dunst] -> [NOT installed!]";
   missing=1;
fi