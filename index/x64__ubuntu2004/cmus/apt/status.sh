#!/usr/bin/env sh
# AUTOGENERATED FILE! DO NOT MODIFY

missing=0;

if $(apt list --installed 'cmus' | grep -q "\[installed\]")
then
   echo "[cmus] -> [installed!]";
else
   echo "[cmus] -> [NOT installed!]";
   missing=1;
fi