#!/usr/bin/env python3
import Bio
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO
from Bio import Align
from Bio.Seq import Seq
# Defina las secuencias
seq1 = "Ecoli_pho_mutbeta.fasta"
seq2 = "Ecoli_phoA_mutalpha.fasta"
seq3 = "Ecoli_phoA.fasta"
mutbeta=SeqIO.read(seq1, "fasta")
#mutalfa=SeqIO.read(seq2, "fasta")
#Wt=SeqIO.read(seq3, "fasta")
# Defina el tipo de alineamiento (aquí "pairwise")
aligner = Align.PairwiseAligner()

# Defina las penalidades 
aligner.match_score = 1
aligner.mismatch_score = -1
aligner.open_gap_score = -1  # Gap opening penalty
aligner.extend_gap_score = -1  # Gap extension penalty

# Realice el alineamiento con las dos secuencias
#alignments1 = aligner.align(Wt, mutalfa)
#alignments2 = aligner.align(Wt, mutbeta)
# Revise los alineamientos (cuantos?)
#for alignment in alignments1:
#    print(alignment)
 #   print(alignment.score)
#for alignment in alignments2:
  #  print(alignment)
   # print(alignment.score)
