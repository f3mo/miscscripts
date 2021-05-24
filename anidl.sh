#!/usr/bin/bash
# DL for gnupluslinux.com
url=$1
links=($(curl $1 | grep -o -P '(\d|\w)*.(jpg|webm|mp4|png)' ))
for i in "${links[@]}"
do
  sleep 2
  wget "$1$i"
done
