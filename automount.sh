#!/bin/bash

# Mounts external HDD in /media/
dir="/media/user/"
check=$(ls $dir)
logfile="/tmp/mountlog.txt"
ext=$(blkid | grep -i /dev/sdb)
while true;
do
  sleep 2m
  if [[ -z "$check" ]]  &&  [[ ! -z "$ext" ]];
  then
    mount -a 
    echo " $(date) PID: $$ sdb has been  mounted in $dir" >> "$logfile"
  else
    :
  fi
done
