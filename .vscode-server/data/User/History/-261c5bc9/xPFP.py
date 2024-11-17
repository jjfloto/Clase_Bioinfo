#!/usr/bin/env python3
#script para clase de alineamiento
import Bio
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO
#definiendo secuencias
sec1=SeqIO.read("nNeandertal_DNA_mit.fasta", "fasta")
sec2=Seq("CTAAGGGTCGAAGGTGGATTTAG")
from Bio import Align
#importamos libreria de alineamiento
alineador=Align.PairwiseAligner()
#funcion alinea pares
alineador2_1=alineador.align(sec2, sec1)
#lista de alineamientos posibles entre secuencias
for alineamiento in sorted(alineador2_1):
    print("Score = %.1f:" % alineamiento.score)
    print(alineamiento)
    print(alineamiento.score)
