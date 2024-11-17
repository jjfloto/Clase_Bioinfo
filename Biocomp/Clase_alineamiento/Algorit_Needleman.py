#!/usr/bin/env python3
from Bio import Align
from Bio.Seq import Seq

# Defina las secuencias
seq1 = Seq("GATTACA")
seq2 = Seq("GCATGCG")

# Defina el tipo de alineamiento (aquí "pairwise")
aligner = Align.PairwiseAligner()

# Defina las penalidades 
aligner.match_score = 1
aligner.mismatch_score = -1
aligner.open_gap_score = -1  # Gap opening penalty
aligner.extend_gap_score = -1  # Gap extension penalty

# Realice el alineamiento con las dos secuencias
alignments = aligner.align(seq1, seq2)

# Revise los alineamientos (cuantos?)
for alignment in alignments:
    print(alignment)
    print(alignment.score)
