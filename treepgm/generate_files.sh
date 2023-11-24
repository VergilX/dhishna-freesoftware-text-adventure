#!/bin/zsh

# Used to create dummy files with similar names
# Author: @abhinanddmanoj

path="$1"
file="$2"
ext="$3"
n=$4

for i in {1..$n}
do
    # echo "${path}/${file}${i}.${ext}"
    echo "${path}/${file}${i}.${ext}" > ${path}/${file}${i}.${ext}
done
