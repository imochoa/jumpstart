#!/usr/bin/env sh
# <<<AUTOGENERATED - DO NOT MODIFY>>>
#		 > UPSTREAM-VER.SH
#		 > TeX Studio
#		 > apt

printf "texlive-fonts-extra > %s\n" "$(apt-cache policy texlive-fonts-extra | grep Candidate | cut -d: -f2 | tr -d /" /")"
printf "texlive-full > %s\n" "$(apt-cache policy texlive-full | grep Candidate | cut -d: -f2 | tr -d /" /")"
printf "texlive-latex-extra > %s\n" "$(apt-cache policy texlive-latex-extra | grep Candidate | cut -d: -f2 | tr -d /" /")"
printf "texlive-xetex > %s\n" "$(apt-cache policy texlive-xetex | grep Candidate | cut -d: -f2 | tr -d /" /")"
printf "texstudio > %s\n" "$(apt-cache policy texstudio | grep Candidate | cut -d: -f2 | tr -d /" /")"
