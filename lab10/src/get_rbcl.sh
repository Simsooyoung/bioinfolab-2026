
#!/bin/bash
# 식물 8종의 rbcL 서열을 NCBI E-utilities 로 받는다 (FASTA + GenBank)
# 사용법: cd lab10 && bash src/get_rbcl.sh

BASE=https://eutils.ncbi.nlm.nih.gov/entrez/eutils
OUT=data

# 학명|파일 이름
SPECIES="Arabidopsis thaliana|rbcL_arabidopsis
Panax ginseng|rbcL_ginseng
Oryza sativa|rbcL_rice
Zea mays|rbcL_maize
Ginkgo biloba|rbcL_ginkgo
Pinus thunbergii|rbcL_pine
Adiantum capillus-veneris|rbcL_fern
Marchantia polymorpha|rbcL_liverwort"

echo "$SPECIES" | while IFS='|' read -r ORG NAME; do
    TERM="rbcL[Gene] AND \"$ORG\"[Organism] AND 1300:1500[SLEN]"
    QUERY=$(echo "$TERM" | sed 's/ /+/g; s/"/%22/g; s/\[/%5B/g; s/\]/%5D/g; s/:/%3A/g')

    # 1) esearch: 첫 번째 결과만 (retmax=1)
    ID=$(wget -q -O - "$BASE/esearch.fcgi?db=nuccore&retmax=1&term=$QUERY" | grep -o '<Id>[0-9]*</Id>' | head -1 | sed 's/<[^>]*>//g')
    sleep 1

    if [ -z "$ID" ]; then
        echo "$ORG: 검색 결과 없음" >&2
        continue
    fi

    # 2) FASTA
    wget -q -O "$OUT/$NAME.fa" "$BASE/efetch.fcgi?db=nuccore&id=$ID&rettype=fasta&retmode=text"
    sleep 1

    # 3) GenBank
    wget -q -O "$OUT/$NAME.gb" "$BASE/efetch.fcgi?db=nuccore&id=$ID&rettype=gb&retmode=text"
    sleep 1

    echo "$ORG -> $NAME (id $ID)"
done
