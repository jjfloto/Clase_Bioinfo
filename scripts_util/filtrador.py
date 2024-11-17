#!/usr/bin/env python3
#este script se crea para detetcatar que secuencias tiene mas de 100 aminoacidos
#librerias
import Bio
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
import sys
import os

#procesamiento input
proteins="CytBProt.txt"
#For para iterar en cada proteina
for R in SeqIO.parse(proteins, "fasta"):
 size=len(R.seq)
 if size > 100:
  print("el organismo", R.id,"tiene", size, "a.a")
  print(R.description.split())
