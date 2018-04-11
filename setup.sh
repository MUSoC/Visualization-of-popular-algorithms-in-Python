#!/bin/bash
if [ $(uname -s) == "Linux" ]; then
  declare -a distributions=("Manjaro" "Ubuntu" "Arch");
  declare -a distpackagemgrs=("1" "0" "1");
  declare -a packagemgr=("apt-get" "pacman");

  dist_count=${#distributions[*]}
  usable_mgr="-1"

  dist_name=$(lsb_release -a);

  for (( i=0; i<=$(( $dist_count -1 )); i++ ))
  do
      if [ $(echo "$dist_name" | grep -c "${distributions[$i]}") -gt 0 ]; then
          usable_mgr=${distpackagemgrs[$i]}
          echo "Found Distribution ${distributions[$i]}, will use ${packagemgr[usable_mgr]}"
      fi
  done

  if [ $usable_mgr == "-1" ]; then
      echo "Err: Linux distibution unknown, will use apt-get"
      usable_mgr="0"
  fi

  case $usable_mgr in
      "0")
      echo "-- apt-get install --"
      sudo apt-get install python2.7-dev python-pip -y

      ;;
      "1")
      echo "-- pacman installation --"
      sudo pacman -S python2 python-pip -y

      ;;
  esac
fi

if [ $(uname -s) == "Darwin" ]; then
  sudo easy_install pip

fi

sudo pip2 install matplotlib
sudo pip2 install networkx




