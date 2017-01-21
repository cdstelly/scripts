#!/bin/bash
find ./ -type f -size +3G -name *E01 -exec ls -lh {} \; 2> /dev/null
