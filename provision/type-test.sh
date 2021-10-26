#!/usr/bin/env bash

# The first argument should be the directory name to test (apt, snap, deb, bin, src...)
altname=$1

# https://stackoverflow.com/questions/46247032/how-to-solve-invoke-rc-d-policy-rc-d-denied-execution-of-start-when-building
printf '#!/bin/sh\nexit 0' > /usr/sbin/policy-rc.d

# For (invoke-rc.d: could not determine current runlevel)
export RUNLEVEL=1


# cd to the correct index dir first...
topdir="$(pwd)";

for p in **/$altname
do

  cd "$topdir/$p"

  if [ -f "./passed" ]; then
    printf "\n$p already passed";
    continue
  fi

  printf "\n\n\n...Running $p\n" ;

  if [ ! -f "./install.sh" ]; then
    printf "\n$p does not have an installation candidate!";
    continue
  fi

  printf "\n\n...INSTALL Testing $p\n" ;
  . "./install.sh" 2>&1 | tee "./install.log"
  . "./status.sh"

  if [ "$missing" -ne "0" ];
  then
      exit 1;
  fi


  printf "\n\n...VER Testing $p\n" ;

  printf "\n\n...REMOVE Testing $p\n" ;
  . "./remove.sh" 2>&1 | tee "./remove.log"
  . "./status.sh"
  if [ "$missing" -eq "0" ];
  then
      exit 1;
  fi

  touch "./passed";

done

printf "\n\nDONE!\n\n"
