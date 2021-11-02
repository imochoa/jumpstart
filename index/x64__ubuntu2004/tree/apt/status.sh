#!/usr/bin/env sh
# AUTOGENERATED FILE! DO NOT MODIFY

missing=0;

if $(apt list --installed 'tree' | grep -q "\[installed\]")
then
   echo "[tree] -> [installed!]";
else
   echo "[tree] -> [NOT installed!]";
   missing=1;
fi