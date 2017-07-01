#!/bin/bash
# for ntfs parsing
joachim_out=$1

cat $1 | grep o\\: | grep -v \$BadClus > image.extract
