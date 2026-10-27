# lab07 정리: 파이썬 함수와 모듈로 FASTA 다루기

## 1. 학습 목표

- `def`로 함수를 만들고 `print`와 `return`의 차이를 이해한다.
- 자주 쓰는 함수를 `fasta.py` 모듈로 모으고 `from fasta import ...`로 재사용한다.
- `if __name__ == "__main__":`으로 모듈 테스트 코드를 분리한다.
- 파일 쓰기(`"w"`, `"a"`)로 FASTA/TSV 결과를 저장한다.

## 2. 폴더 구조

```
lab07/
├── data/   seqs.fasta, seqs2.fasta, lower.fasta (입력 서열)
├── doc/    summary.tsv, summary2.tsv, long.fasta (결과물)
└── src/    파이썬 스크립트, README.md, python_cheatsheet.md
```

## 3. 함수 기초

| 파일 | 내용 |
|---|---|
| `fseqlen.py` | `print`만 하는 함수는 `None`을 돌려주고, `return`하는 함수는 값을 돌려준다는 비교 |
| `fgc.py` | 첫 GC 비율 함수 `gc_content(seq)` 만들기 |
| `seqlen2.py` | 함수 없이 FASTA를 읽어 서열별 길이 출력 |
| `filter.py` | 길이 20~40, GC 0.4~0.6인 서열만 골라 출력 (함수 없이 작성) |

## 4. `fasta.py` 모듈

| 함수 | 설명 |
|---|---|
| `read_fasta(filename)` | FASTA를 읽어 `{이름: 서열}` 딕셔너리로 반환. 헤더의 첫 단어를 이름으로, 서열은 대문자로 변환 |
| `gc_content(seq)` | GC 비율(0~1) 반환. 빈 서열이면 0.0 |
| `write_fasta(seqs, filename)` | 딕셔너리를 FASTA 파일로 저장 |
| `reverse_complement(seq)` | 역상보 서열 반환 (예: `AATT` → `AATT`, `ATGC` → `GCAT`) |
| `length_stats(seqs)` | 서열 개수, 전체/평균/최단/최장 길이를 딕셔너리로 반환 |

`python3 src/fasta.py data/seqs.fasta`처럼 직접 실행하면 `__main__` 블록이 서열별 길이·GC와 역상보 검증 결과를 출력한다.

## 5. 모듈을 활용한 스크립트

| 스크립트 | 사용법 | 하는 일 |
|---|---|---|
| `countseq2.py` | `python3 countseq2.py <fasta>` | 서열 개수 출력 |
| `filter_fasta.py` | `python3 filter_fasta.py <in> <최소길이> <out>` | 최소 길이 이상인 서열만 새 FASTA로 저장 |
| `summary.py` | `python3 summary.py <fasta> <out.tsv>` | 서열별 `name/length/gc` TSV 저장 |
| `stats.py` | `python3 src/stats.py <fasta>` | `length_stats` 결과를 f-string으로 출력 |
| `batchinfo.py` | `python3 src/batchinfo.py data doc/summary.tsv` | 폴더 안 모든 `*.fasta`를 `glob`으로 돌며 파일별 개수·전체 길이·평균 GC를 TSV로 저장 |

`stats.py`, `batchinfo.py`는 `sys.path.insert(0, "src")`로 lab07 폴더에서 실행해도 `fasta` 모듈을 찾게 했다.

## 6. 결과물

`doc/long.fasta` — `seqs.fasta`에서 길이 기준을 넘는 gene1(30bp), gene3(22bp)만 저장 (gene2 15bp 제외).

`doc/summary.tsv` — `batchinfo.py` 결과:

| file | count | total | mean_gc |
|---|---|---|---|
| data/lower.fasta | 2 | 20 | 0.65 |
| data/seqs.fasta | 3 | 67 | 0.504 |
| data/seqs2.fasta | 2 | 16 | 0.25 |

`lower.fasta`는 소문자 서열이지만 `read_fasta`가 대문자로 바꾸기 때문에 GC가 올바르게 계산된다.

## 7. 핵심 개념 (cheatsheet 요약)

- **함수 정의**: `def 이름(매개변수):` 다음 줄부터 들여쓰기.
- **print vs return**: `return`은 값을 돌려주고 함수를 끝내며, `print`는 화면에 보여주기만 한다.
- **import**: `from 모듈 import 함수`로 다른 파일의 함수를 가져온다.
- **`__name__ == "__main__"`**: 파일을 직접 실행할 때만 동작하고, import할 때는 실행되지 않는다.
- **파일 모드**: `"w"`는 덮어쓰기(bash `>`), `"a"`는 이어쓰기(bash `>>`).
- **겪은 오류**: 실행 위치에 파일이 있는지 확인할 것, 들여쓰기를 꼼꼼히 볼 것.

## 8. 남은 과제 / 개선점

- `reverse_complement`에 `return comp`가 빠져 있어 `None`을 돌려준다. 또 `A/T/G/C` 이외 문자(N 등)가 있으면 `KeyError`가 난다.
- `fasta.py`의 `__main__` 블록이 `reverse_complement` 정의보다 위에 있어 직접 실행 시 `NameError`가 난다. `__main__` 블록을 파일 맨 아래로 옮겨야 한다.
- 추가하고 싶은 함수: 서열 내 A/T/G/C 개수를 세는 함수.
