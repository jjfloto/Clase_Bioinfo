#!/usr/bin/env python3
#script para clase de alineamiento
import Bio
from Bio.Seq import Seq
#definiendo secuencias
sec1=Seq("ACGTG")
sec2=Seq("ACGTC")
sec3=Seq("ACGCC")
from Bio import Align #importamos libreria de alineamiento
alineador=Align.PairwiseAligner()
#funcion alinea pares
alineador1_2=alineador.align(sec1, sec2)
#lista de alineamientos posibles entre secuencias
print("paso 1")
for alineamiento in sorted(alineador1_2):
   print("Score = %.1f:" % alineamiento.score)
   print(alineamiento)
print("paso 2")
for alineamiento in sorted(alineador1_2):
    print(alineamiento)
    print(alineamiento.score)
print("paso 3")
alineador.match_score = 1
alineador.mismatch_score = -1
alineador.open_gap_score = -1

for alignment in sorted(alineador1_2): 
    print(alignment)
    print(alignment.score) 
