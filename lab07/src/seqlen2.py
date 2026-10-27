import sys
 
filename = sys.argv[1]
 
lengths = {}
name = None
 
with open(filename) as f:
    for line in f:
        line = line.rstrip()
        if line.startswith(">"):
            name = line[1:].split()[0]
            lengths[name] = 0
        else:
            lengths[name] = lengths[name] + len(line)
 
for name in lengths:
    print(name, lengths[name])

