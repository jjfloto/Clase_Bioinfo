#!/usr/bin/env python3
import Bio
from Bio.Seq import Seq
from Bio import Align
from Bio import SeqIO
# Defina las secuencias
seq1f = next(SeqIO.parse("secAA_Emy.fasta", "fasta"))
seq2f= next(SeqIO.parse("NCBI_Prot_Emydura.fasta", "fasta"))
seq1=seq1f.seq
seq2=seq2f.seq
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
# Mostrar los resultados de los alineamientos
for alignment in alignments:
    print(alignment)
    print("la puntación fue:",alignment.score)
