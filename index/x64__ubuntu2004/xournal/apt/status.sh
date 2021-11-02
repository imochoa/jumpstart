#!/usr/bin/env sh
# AUTOGENERATED FILE! DO NOT MODIFY

missing=0;

if $(apt list --installed 'xournalpp' | grep -q "\[installed\]")
then
   echo "[xournalpp] -> [installed!]";
else
   echo "[xournalpp] -> [NOT installed!]";
   missing=1;
fi