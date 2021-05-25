#!/usr/bin/env sh

# DO NOT MODIFY!
# THIS FILE WAS AUTOGENERATED BY *generate-status-files.py*

missing=0;


if $(apt list --installed 'texstudio' | grep -q "\[installed\]")
then
   echo "[texstudio] -> [installed!]";
else
   echo "[texstudio] -> [NOT installed!]";
   missing=1;
fi


if $(apt list --installed 'texlive-latex-extra' | grep -q "\[installed\]")
then
   echo "[texlive-latex-extra] -> [installed!]";
else
   echo "[texlive-latex-extra] -> [NOT installed!]";
   missing=1;
fi


if $(apt list --installed 'texlive-xetex' | grep -q "\[installed\]")
then
   echo "[texlive-xetex] -> [installed!]";
else
   echo "[texlive-xetex] -> [NOT installed!]";
   missing=1;
fi


if [ "$missing" -eq "0" ];
then
    exit 0;
else
    exit 1;
fi

