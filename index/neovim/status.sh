#!/usr/bin/env sh
missing=0;


if $(apt list --installed 'wget' | grep -q "\[installed\]")
then
   echo "[wget] -> [installed!]";
else
   echo "[wget] -> [NOT installed!]";
   missing=1;
fi


if $(apt list --installed 'curl' | grep -q "\[installed\]")
then
   echo "[curl] -> [installed!]";
else
   echo "[curl] -> [NOT installed!]";
   missing=1;
fi


if $(apt list --installed 'git' | grep -q "\[installed\]")
then
   echo "[git] -> [installed!]";
else
   echo "[git] -> [NOT installed!]";
   missing=1;
fi


if $(apt list --installed 'xclip' | grep -q "\[installed\]")
then
   echo "[xclip] -> [installed!]";
else
   echo "[xclip] -> [NOT installed!]";
   missing=1;
fi


if $(apt list --installed 'exuberant-ctags' | grep -q "\[installed\]")
then
   echo "[exuberant-ctags] -> [installed!]";
else
   echo "[exuberant-ctags] -> [NOT installed!]";
   missing=1;
fi


if $(apt list --installed 'ncurses-term' | grep -q "\[installed\]")
then
   echo "[ncurses-term] -> [installed!]";
else
   echo "[ncurses-term] -> [NOT installed!]";
   missing=1;
fi


if $(apt list --installed 'python3-pip' | grep -q "\[installed\]")
then
   echo "[python3-pip] -> [installed!]";
else
   echo "[python3-pip] -> [NOT installed!]";
   missing=1;
fi


if $(apt list --installed 'python3-autopep8' | grep -q "\[installed\]")
then
   echo "[python3-autopep8] -> [installed!]";
else
   echo "[python3-autopep8] -> [NOT installed!]";
   missing=1;
fi


if [ "$missing" -eq "0" ];
then
    exit 0;
else
    exit 1;
fi


