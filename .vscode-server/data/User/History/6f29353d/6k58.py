#!/usr/bin/env python3
import Bio
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO
from Bio import Align
from Bio.Seq import Seq
# Defina las secuencias
seq1 = "Ecoli_phoA_mutbeta.fasta"
seq2 = "Ecoli_phoA_mutalpha.fasta"
seq3 = "Ecoli_phoA.fasta"
mutbeta=SeqIO.read(seq1, "fasta")
mutalfa=SeqIO.read(seq2, "fasta")
Wt=SeqIO.read(seq3, "fasta")
#enmascaramiento para obtener el traducido
protWT=Wt.seq.translate()
protB=mutbeta.seq.translate()
protA=mutalfa.seq.translate()
# Defina el tipo de alineamiento (aquí "pairwise")
aligner = Align.PairwiseAligner()

# Defina las penalidades 
aligner.match_score = 1
aligner.mismatch_score = -1
aligner.open_gap_score = -1  # Gap opening penalty
aligner.extend_gap_score = -1  # Gap extension penalty

# Realice el alineamiento con las dos secuencias
alignments1 = aligner.align(protWT, protB, protA)
#alignments2 = aligner.align(protWT, protA)
# Revise los alineamientos (cuantos?)
print("Proteinas de Beta")
for alignment in alignments1:
   print(alignment)
   print(alignment.score)
print("Proteinas alfa")
#for alignment in alignments2:
   # print(alignment)
   # print(alignment.score)
