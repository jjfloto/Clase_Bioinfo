#!/usr/bin/env python3
#el siguiente script es para secuencias
#liberias clave
import Bio
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO
import os
import sys

dna="CytBDNA.txt"
for R in SeqIO.parse(dna, "fasta"):
 print("el id es:", R.id,"su # de nc es:", len(R.seq))
 mRNA=R.seq.transcribe()
 prot=mRNA.translate("Vertebrate Mitochondrial")
 print("longitud de mRNA", len(mRNA))
 print("longitud de proteina", len(prot))
