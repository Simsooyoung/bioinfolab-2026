import sys
def read_fasta(filename):
    """FASTA 파일을 읽어 {이름: 서열} 딕셔너리로 돌려준다."""
    seqs = {}
    name = None
    with open(filename) as f:
        for line in f:
            line = line.rstrip()
            if line.startswith(">"):
                name = line[1:].split()[0]
                seqs[name] = ""
            else:
                seqs[name] = seqs[name] + line
    return seqs

 
filename = sys.argv[1]
 
seqs = {}
name = None
with open(filename) as f:
    for line in f:
        line = line.rstrip()
        if line.startswith(">"):
            name = line[1:].split()[0]
            seqs[name] = ""
        else:
            seqs[name] = seqs[name] + line
 
for name in seqs:
    seq = seqs[name]
    length = len(seq)
    gc = (seq.count("G") + seq.count("C")) / length
 
    if length >= 20 and length <= 40 and gc >= 0.4 and gc <= 0.6:
        print(name, length, round(gc, 3))

