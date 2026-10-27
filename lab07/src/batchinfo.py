import sys
import glob
sys.path.insert(0, "src")
from fasta import read_fasta, gc_content, length_stats

folder = sys.argv[1]
outfile = sys.argv[2]

with open(outfile, "w") as out:
    out.write("file\tcount\ttotal\tmean_gc\n")
    for path in sorted(glob.glob(folder + "/*.fasta")):
        seqs = read_fasta(path)
        stats = length_stats(seqs)
        gc_values = [gc_content(seq) for seq in seqs.values()]
        mean_gc = sum(gc_values) / len(gc_values)
        out.write(f"{path}\t{stats['count']}\t{stats['total']}\t{round(mean_gc, 4)}\n")