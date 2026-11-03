import os
import sys

# lab07/src 의 fasta.py 를 불러올 수 있게 경로를 추가한다
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "..", "lab07", "src"))
from fasta import read_fasta

if len(sys.argv) != 2:
    print("사용법: python3 src/count_agent2.py <FASTA 파일>")
    sys.exit(1)

seqs = read_fasta(sys.argv[1])
print(len(seqs))
