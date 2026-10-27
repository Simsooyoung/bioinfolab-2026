fasta.py 에 들어 있는 함수 목록
 1. def read_fasta(filename):
    FASTA 파일을 읽어 {이름: 서열} 딕셔너리로 돌려준다.
 2. def gc_content(seq):
    서열의 총길이 대비 GC 비율을 0과 1 사이의 수로 돌려준다.
 3. def write_fasta(seqs, filename):
    {이름: 서열} 딕셔너리를 FASTA 파일로 저장한다.
 4. def reverse_complement(seq):
    서열의 역상보 서열을 돌려준다. 예를 들어 AATT이면 TTAA로
 5. def length_stats(seqs):
    서열 딕셔너리의 길이 통계(서열 개수, 전체 길이, 평균 길이, 최단 길이, 최장 길이)를 돌려준다.

아직 부족하다고 느끼는 점이나 추가하고 싶은 함수
 1. 서열 내 ATGC 개수를 세어주는 함수
