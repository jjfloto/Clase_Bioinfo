#!/usr/bin/env python3
# Script por Laura Salazar Jaramillo
# Busca la secuencia de proteinas del citocromo B de neanderthales


from Bio import Entrez
from Bio import SeqIO

Entrez.email = "juan.florez87@eia.edu.co"

with Entrez.efetch(
    db="protein", rettype="fasta", retmode="text", id="YP_002124314.2") as handle:
    seq_record = SeqIO.read(handle, "fasta")

print(seq_record)
SeqIO.write(seq_record, "hsneanderthal_cytb_prot.fa", "fasta")
