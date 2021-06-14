#!/bin/bash



MAX=976
current=$(cat $HOME/backlight)
add=45
append=$(( $add+$current ))



if [ "$append" -lt "$MAX" ]; then
    echo  $append  > $HOME/backlight

fi
