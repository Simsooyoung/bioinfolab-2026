#!/usr/bin/bash

FILE=$1

if [ ! -f "$FILE" ]
then
    echo "파일이 없습니다: $FILE"
    exit 1
fi

awk '
/^>/ {
    if (name) print name, len
    name = substr($0, 2)
    len = 0
    next
}
{
    gsub(/[[:space:]]/, "")
    len += length($0)
}
END {
    if (name) print name, len
}
' "$FILE"