#!/usr/bin/env python3
#script para punto 6
import Bio
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
alfa="Ecoli_phoA_mutalpha.fasta"
beta="Ecoli_phoA_mutbeta.fasta"
#para alfa
for record in SeqIO.parse(alfa, "fasta"):
 print(record.id)
 print("con un tamaño de nc de", len(record.seq))
 print(record)
#para beta
for record in SeqIO.parse(beta, "fasta"):
 print(record.id)
 print("con un tamaño de nucleotidos de", len(record.seq))
 print(record)
#tamaño de pares de bases
mutalfa=SeqIO.read(alfa, "fasta")
mutbeta=SeqIO.read(beta, "fasta")
#print("numero de codones en mutante alfa", len(mutalfa.seq)/3)
#print("numero de codones en mutante beta", len(mutbeta.seq)/3)
#corecciones
print("numero de aminoacidos en alfa:", len(mutalfa.seq.translate()))
print("numero de aminoacidos en beta:", len(mutbeta.seq.translate()))
