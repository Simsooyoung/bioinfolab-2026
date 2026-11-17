import sys

def read_fastq(filename):
    records = []
    with open(filename) as f:
        lines = f.readlines()
    for i in range(0, len(lines), 4):
        name = lines[i].rstrip()[1:]
        seq = lines[i + 1].rstrip().upper()
        qual = lines[i + 3].rstrip()
        records.append((name, seq, qual))
    return records

# lab07/src/fasta.py 의 gc_content 와 같은 함수
def gc_content(seq):
    if len(seq) == 0:
        return 0.0
    gc = seq.count("G") + seq.count("C")
    return gc / len(seq)

def mean_quality(qual):
    if len(qual) == 0:
        return 0.0
    total = 0
    for ch in qual:
        total = total + ord(ch) - 33
    return total / len(qual)

def average(values):
    return sum(values) / len(values)

def print_group(title, rows, overall):
    print()
    print(title)
    print("name\tgc\tmean_quality")
    for name, gc, q in rows:
        print(name + "\t" + str(round(gc, 3)) + "\t" + str(round(q, 2)))
    group_mean = average([q for name, gc, q in rows])
    print("그룹 평균 품질:", round(group_mean, 2),
          "(전체 평균과 차이:", round(group_mean - overall, 2), ")")

reads = read_fastq(sys.argv[1])
n = 10

# read마다 (이름, GC 비율, 평균 품질)
rows = []
for name, seq, qual in reads:
    rows.append((name.split()[0], gc_content(seq), mean_quality(qual)))

# 두 번째 인자를 주면 read별 결과를 TSV 파일로 저장
if len(sys.argv) > 2:
    with open(sys.argv[2], "w") as out:
        out.write("name\tgc\tmean_quality\n")
        for name, gc, q in rows:
            out.write(name + "\t" + str(round(gc, 4)) + "\t" + str(round(q, 2)) + "\n")

overall_gc = average([gc for name, gc, q in rows])
overall_q = average([q for name, gc, q in rows])
print("read 개수:", len(rows))
print("전체 평균 GC 비율:", round(overall_gc, 3))
print("전체 평균 품질:", round(overall_q, 2))

rows_by_gc = sorted(rows, key=lambda r: r[1])
print_group("GC 비율이 가장 낮은 read " + str(n) + "개", rows_by_gc[:n], overall_q)
print_group("GC 비율이 가장 높은 read " + str(n) + "개", rows_by_gc[-n:][::-1], overall_q)
