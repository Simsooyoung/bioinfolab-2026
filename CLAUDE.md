# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

A student's weekly lab repository for a bioinformatics lab course (생물정보학실험). It is not an application: there is no build, lint, or test suite. Each `labNN/` folder is one week's exercises: small Bash and Python scripts that process FASTA/text files. 

## Layout conventions

- New weeks are created by copying the template: `cp -r lab-template labNN`. Every lab has the same three folders:
  - `data/`: input data (downloaded or generated)
  - `doc/`: reports, result summaries (e.g. `.tsv`), figures, and write-ups such as `lab09/doc/lab07.md`
  - `src/`: the student's own `.sh` / `.py` scripts
- Scripts are run from the lab folder with paths relative to it, e.g. `cd lab07 && python3 src/summary.py data/seqs.fasta doc/summary.tsv`.
- The `$MYHOME` env var (set by the devcontainer) points to the workspace root, and plain `cd` returns there.
- `resources/` is empty scaffolding. `my/`, `myproject/`, `project/`, and `my project/` are leftover practice directories.
- Sequencing data (`*.fastq*`, `*.sra`) and assembly/annotation outputs (shovill/spades/prokka/flye dirs, FastQC reports) are gitignored on purpose. They are re-downloaded with `wget` when needed, so never commit them.

## Python code

- Scripts are deliberately simple teaching code: they use only the standard library, read CLI args through `sys.argv`, and avoid argparse, classes, and third-party packages unless the lab calls for them. Match that level.
- `lab07/src/fasta.py` is the shared FASTA helper module: `read_fasta` returns `{name: SEQ}`, using the first header word and uppercasing the sequence. It also has `gc_content`, `write_fasta`, `reverse_complement`, and `length_stats`. Sibling scripts import it with `from fasta import ...`, so run them from a directory where `src/` is on the import path, i.e. `python3 src/script.py` from the lab folder. Its `__main__` block is the module's self-test: `python3 src/fasta.py data/seqs.fasta`.
- Function docs for the module live in `lab07/src/README.md` and the week summary in `lab09/doc/lab07.md`. Update them if you change the module's API.

## Environment (devcontainers)

`.devcontainer/` has four Codespaces configs that use prebuilt `ghcr.io/goshng/bioinfolab:*` images. Which tools are on PATH depends on the config:

| Config | Weeks | Tools |
|---|---|---|
| `1-basic` | 02–07 | python3, coreutils |
| `2-conda` | conda week | micromamba (students install packages themselves) |
| `3-seq` | 08–09, 12–14 | seqkit, blast, mafft, iqtree, fastqc, fastp |
| `4-genome` | 10–11 | the above plus shovill, prokka |

Run `bash .devcontainer/check.sh` to see which tools this environment has. Outside the conda week, don't install missing tools; the course rule is to report them to the instructor.

## Workflow

At the end of each lab the student commits and pushes (`git add . && git commit -m "labNN 완료" && git push`). Commit messages are short Korean notes.

## 규칙
- FASTA 파일은 fasta.py 함수를 사용한다
- 새 라이브러리를 쓰기 전에 허용 여부를 묻는다
- 하지 말아야 할 명령어: `rm -rf`, `chmod 777`
- 커밋 전에 반드시 `git status` 로 변경 파일을 확인한다