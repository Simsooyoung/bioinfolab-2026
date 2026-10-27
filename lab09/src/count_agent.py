import sys

if len(sys.argv) != 2:
    print("사용법: python count_agent.py <FASTA 파일>")
    sys.exit(1)

count = 0
with open(sys.argv[1]) as f:
    for line in f:
        if line.startswith(">"):
            count += 1

print(count)
