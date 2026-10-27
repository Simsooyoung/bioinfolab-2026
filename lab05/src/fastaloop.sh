#!/usr/bin/bash

DIR=$1
#!/usr/bin/bash

DIR=$1

if [ ! -d "$DIR" ]; then
    echo "오류: $DIR 폴더가 존재하지 않습니다"
    exit 1
fi

if [ ! -f "$DIR"/*.fasta ]; then
    echo "오류: $DIR 폴더에 FASTA 파일이 없습니다"
    exit 1
fi

echo "file        count"
for F in $DIR/*.fasta
do
    NAME=$(basename $F)
    COUNT=$(grep -c '>' $F)
    echo "$NAME  $COUNT"
done