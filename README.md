# MagnumOpus: In-Silico PCR and Sequence Alignment Tool

MagnumOpus is a Python package designed for in-silico PCR and sequence alignment tasks. It uses BLAST to identify and extract amplicons from DNA sequences based on provided primers, and then aligns these amplicons using the Needleman-Wunsch algorithm. The package allows users to compare genetic sequences efficiently, highlighting similarities and differences in nucleotide arrangements. Key components include scripts for testing the core functions (ispcr and needleman_wunsch), as well as a main script (amplicon_align.py) for performing comprehensive sequence analysis. This project is particularly useful for bioinformatics research involving comparative genomics and genetic sequence analysis.

## Description
- **amplicon_align.py:** Script to perform in-silico PCR on two DNA assemblies, align the resulting amplicons, and print the best alignment and score.
- **data/:** Directory containing sample DNA sequence files in FASTA format.
- **magnumopus/:** The core Python package containing modules for performing in-silico PCR (ispcr.py) and sequence alignment (nw.py).
- **q1.py:** A test script that demonstrates how to use the ispcr function to find amplicons in a DNA assembly.
- **q2.py:** A test script that demonstrates how to use the needleman_wunsch function to align two DNA sequences.

## Requirements
To use MagnumOpus, ensure you have the following dependencies installed:

- Python 3.8+
- BLAST (installed and accessible via the command line)
- seqtk (installed and accessible via the command line)

## Example Usage
```sh
python3 amplicon_align.py -1 data/Pseudomonas_aeruginosa_PAO1.fna -2 data/Pseudomonas_protegens_CHA0.fna -p data/rpoD.fna -m 2000 --match 1 --mismatch -1 --gap -1
```

Command Line Arguments:
- -1, --assembly1: Path to the first assembly file (required).
- -2, --assembly2: Path to the second assembly file (required).
- -p, --primers: Path to the primer file (required).
- -m, --max_amplicon_size: Maximum amplicon size for isPCR (required).
- --match: Match score to use in alignment (required).
- --mismatch: Mismatch penalty to use in alignment (required).
- --gap: Gap penalty to use in alignment (required).
