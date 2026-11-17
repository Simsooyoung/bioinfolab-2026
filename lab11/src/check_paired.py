import sys

# 사용법: python3 src/check_paired.py data/SRR1553607_1.fastq data/SRR1553607_2.fastq
# 두 paired-end FASTQ 파일의
#   1) read 개수가 같은지
#   2) 같은 순서의 read끼리 이름이 짝을 이루는지
# 확인한다.


def read_names(filename):
    # FASTQ는 4줄이 한 read: 1번째 줄(@이름)만 모은다
    names = []
    with open(filename) as f:
        line_no = 0
        for line in f:
            if line_no % 4 == 0:
                names.append(line.rstrip()[1:])
            line_no = line_no + 1
    return names


def base_name(header):
    # 헤더의 첫 단어만 사용 (예: "SRR1553607.1 1 length=101" -> "SRR1553607.1")
    name = header.split()[0]
    # 옛 Illumina 형식은 이름 끝에 /1, /2 가 붙는다 (예: read123/1, read123/2)
    # 마지막 숫자와 기호를 떼고 비교한다
    if name.endswith("/1") or name.endswith("/2"):
        name = name[:-2]
    return name


names1 = read_names(sys.argv[1])
names2 = read_names(sys.argv[2])

print("file1 reads:", len(names1))
print("file2 reads:", len(names2))

if len(names1) == len(names2):
    print("read 개수: 같음")
else:
    print("read 개수: 다름")

# 짧은 쪽 길이만큼 같은 순서끼리 비교
n = min(len(names1), len(names2))
mismatch = 0
for i in range(n):
    if base_name(names1[i]) != base_name(names2[i]):
        mismatch = mismatch + 1
        if mismatch <= 5:
            print("짝이 안 맞음 #" + str(i + 1) + ": " + names1[i] + " | " + names2[i])

print("비교한 쌍:", n)
print("이름이 다른 쌍:", mismatch)

if len(names1) == len(names2) and mismatch == 0:
    print("결과: OK, 두 파일이 올바르게 짝을 이룬다")
else:
    print("결과: FAIL, 짝이 맞지 않는다")
