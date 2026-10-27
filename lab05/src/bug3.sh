#!/usr/bin/bash
 
OUT=${1:-result}
mkdir -p $OUT
echo "결과" > $OUT/result.txt
cat $OUT/result.txt

