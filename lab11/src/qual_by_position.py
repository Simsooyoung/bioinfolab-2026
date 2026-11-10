import sys

def read_fastq(filename):
    records = []
    with open(filename) as f:
        lines = f.readlines()
    for i in range(0, len(lines), 4):
        name = lines[i].rstrip()[1:]
        seq = lines[i + 1].rstrip()
        qual = lines[i + 3].rstrip()
        records.append((name, seq, qual))
    return records

reads = read_fastq(sys.argv[1])

# 위치별 품질 점수 합계와 염기 개수 (trimming 후 read 길이가 달라도 동작)
totals = []
counts = []
for name, seq, qual in reads:
    for i in range(len(qual)):
        if i >= len(totals):
            totals.append(0)
            counts.append(0)
        totals[i] = totals[i] + ord(qual[i]) - 33
        counts[i] = counts[i] + 1

print("position\tcount\tmean_quality")
for i in range(len(totals)):
    mean = totals[i] / counts[i]
    print(str(i + 1) + "\t" + str(counts[i]) + "\t" + str(round(mean, 2)))
