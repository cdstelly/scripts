#!/bin/bash
find ./ -type f -size +3G -name *E01 -exec ls -lh {} \; 2> /dev/null
find ./ -name "*.pdf" -print0 | xargs -0 md5
