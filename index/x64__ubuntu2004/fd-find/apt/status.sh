#!/usr/bin/env sh
# AUTOGENERATED FILE! DO NOT MODIFY

missing=0;

if $(apt list --installed 'fd-find' | grep -q "\[installed\]")
then
   echo "[fd-find] -> [installed!]";
else
   echo "[fd-find] -> [NOT installed!]";
   missing=1;
fi