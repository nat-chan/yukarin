#!/bin/zsh
convert $1 txt:-|sed -e "s/: (/,/g" -e "s/).*//g" -e '1d'
