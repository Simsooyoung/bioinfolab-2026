#!/usr/bin/bash

DIR=$1
QUERY=$2

declare -A COUNT

for F in "$DIR"/*.fasta
do
    COUNT[$(basename "$F")]=$(grep -c '>' "$F")
done

if [ -n "$QUERY" ]
then
    echo "${COUNT[$QUERY]:-해당 이름 없음}"
else
    for K in "${!COUNT[@]}"
    do
        echo "$K ${COUNT[$K]}"
    done
fi