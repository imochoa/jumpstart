#!/usr/bin/env sh
# AUTOGENERATED FILE! DO NOT MODIFY

missing=0;

if $(apt list --installed 'ripgrep' | grep -q "\[installed\]")
then
   echo "[ripgrep] -> [installed!]";
else
   echo "[ripgrep] -> [NOT installed!]";
   missing=1;
fi
