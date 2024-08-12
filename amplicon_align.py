#!/usr/bin/env python3
import argparse
from magnumopus import ispcr, needleman_wunsch

def reverse_complement(seq: str) -> str:
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    filtered_seq = filter(lambda x: x in complement, seq)
    return ''.join(complement[base] for base in filtered_seq)[::-1]

def main(args):
    amplicon1 = ispcr(args.primers, args.assembly1, args.max_amplicon_size)
    amplicon2 = ispcr(args.primers, args.assembly2, args.max_amplicon_size)
    parts1 = amplicon1.split('\n')
    amplicon1 = ''.join(parts1[1:])
    parts2 = amplicon2.split('\n')
    amplicon2 = ''.join(parts2[1:])
    rev_amplicon2 = reverse_complement(amplicon2)
    alignment1, score1 = needleman_wunsch(amplicon1, amplicon2, args.match, args.mismatch, args.gap)
    alignment2, score2 = needleman_wunsch(amplicon1, rev_amplicon2, args.match, args.mismatch, args.gap)
    if score1 > score2:
        for i in alignment1:
            print(i)
        print(score1)
    else:
        for i in alignment2:
            print(i)
        print(score2)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Perform in-silico PCR on two assemblies and align the amplicons')
    parser.add_argument('-1', '--assembly1', required=True, help='Path to the first assembly file')
    parser.add_argument('-2', '--assembly2', required=True, help='Path to the second assembly file')
    parser.add_argument('-p', '--primers', required=True, help='Path to the primer file')
    parser.add_argument('-m', '--max_amplicon_size', required=True, type=int, help='Maximum amplicon size for isPCR')
    parser.add_argument('--match', required=True, type=int, help='Match score to use in alignment')
    parser.add_argument('--mismatch', required=True, type=int, help='Mismatch penalty to use in alignment')
    parser.add_argument('--gap', required=True, type=int, help='Gap penalty to use in alignment')
    args = parser.parse_args()
    main(args)