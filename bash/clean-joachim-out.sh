#!/bin/bash
joachim_out=$1

cat $1 | grep o\\: | grep -v \$BadClus > image.extract
