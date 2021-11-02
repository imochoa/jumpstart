#!/usr/bin/env sh
# AUTOGENERATED FILE! DO NOT MODIFY

missing=0;

if $(apt list --installed 'source-highlight' | grep -q "\[installed\]")
then
   echo "[source-highlight] -> [installed!]";
else
   echo "[source-highlight] -> [NOT installed!]";
   missing=1;
fi