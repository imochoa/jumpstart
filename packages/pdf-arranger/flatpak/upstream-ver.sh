#!/bin/bash

# <<<AUTOGENERATED - DO NOT MODIFY>>>
#		 >     File: upstream-ver.sh
#		 >     Name: PDF Arranger
#		 > Template: flatpak

printf "com.github.jeromerobert.pdfarranger > %s\n" "$(flatpak search com.github.jeromerobert.pdfarranger | head -n1 | cut -f4 | tr -d /" /")"
