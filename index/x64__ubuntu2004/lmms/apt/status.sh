#!/usr/bin/env sh
# AUTOGENERATED FILE! DO NOT MODIFY

missing=0;

if $(apt list --installed 'lmms' | grep -q "\[installed\]")
then
   echo "[lmms] -> [installed!]";
else
   echo "[lmms] -> [NOT installed!]";
   missing=1;
fi