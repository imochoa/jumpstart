#!/bin/bash
set -euo pipefail
IFS=$'\n\t'

# <<<AUTOGENERATED - DO NOT MODIFY>>>
#		 >     File: remove.sh
#		 >     Name: TeX Studio
#		 > Template: apt

sudo apt-get remove -y texlive-fonts-extra texlive-full texlive-latex-extra texlive-xetex texstudio
