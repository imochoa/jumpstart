#!/bin/bash
set -euo pipefail
IFS=$'\n\t'

# <<<AUTOGENERATED - DO NOT MODIFY>>>
#		 >     File: remove.sh
#		 >     Name: python
#		 > Template: apt

sudo apt-get remove -y build-essential libffi-dev libpq-dev libssl-dev libxml2-dev libxslt1-dev pandoc pandoc-citeproc python3 python3-dev python3-pip python3-venv texlive texlive-latex-extra texlive-xetex zlib1g-dev
