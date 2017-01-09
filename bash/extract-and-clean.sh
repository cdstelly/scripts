#!/bin/bash
# assumes is on path: fsntfstools 
# usage: ./extract-and-clean.sh image.raw offset
fsntfstools -E all -o $2 $1 > temp

clean-joachim-out.sh temp

rm temp
