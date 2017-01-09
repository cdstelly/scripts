#!/bin/bash
find ./ -type f -size +2G -name *E01 -exec ls -lh {} \; 2> /dev/null
