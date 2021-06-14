#!/bin/bash

MAX=976
current=$(cat $HOME/backlight)
sub=45
append=$(( $current-$sub ))

echo $append > $HOME/backlight
