import sys
sys.path.insert(0, "src")
from fasta import read_fasta, length_stats

seqs = read_fasta(sys.argv[1])
stats = length_stats(seqs)

print(f"서열 개수: {stats['count']}")
print(f"전체 길이: {stats['total']}")
print(f"평균 길이: {round(stats['mean'], 2)}")
print(f"최단 길이: {stats['min']}")
print(f"최장 길이: {stats['max']}")