"""FASTA 파일을 다루는 함수 모음"""
 
 
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
                seqs[name] = seqs[name] + line.upper()
    return seqs
 
 
def gc_content(seq):
    """서열의 GC 비율을 0과 1 사이의 수로 돌려준다."""
    if len(seq) == 0:
        return 0.0
    gc = seq.count("G") + seq.count("C")
    return gc / len(seq)

 
def write_fasta(seqs, filename):
    """{이름: 서열} 딕셔너리를 FASTA 파일로 저장한다."""
    with open(filename, "w") as out:
        for name in seqs:
            out.write(">" + name + "\n")
            out.write(seqs[name] + "\n")

def reverse_complement(seq):
    """서열의 역상보 서열을 돌려준다."""
    complement = {"A": "T", "T": "A", "G": "C", "C": "G"}
    seq = seq.upper()
    comp = ""
    for base in seq:
        comp = comp + complement[base]

def length_stats(seqs):
    """서열 딕셔너리의 길이 통계를 돌려준다."""
    lengths = [len(seq) for seq in seqs.values()]
    return {
        "count": len(lengths),
        "total": sum(lengths),
        "mean": sum(lengths) / len(lengths),
        "min": min(lengths),
        "max": max(lengths),
    }
    
 
if __name__ == "__main__":
    import sys
    seqs = read_fasta(sys.argv[1])
    for name in seqs:
        print(name, len(seqs[name]), round(gc_content(seqs[name]), 3))
    
     # reverse_complement 검증
    for name in seqs:
        seq = seqs[name]
        if reverse_complement(reverse_complement(seq)) == seq:
            print(name, "OK")
        else:
            print(name, "FAIL")
