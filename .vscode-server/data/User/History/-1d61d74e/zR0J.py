#!/usr/bin/env python3
import Bio

from Bio.Seq import Seq
sec=Seq("ATATCGTGCGCGCTA")
transcrito= sec.transcribe()
traducido=sec.translate()
traducido2=transcrito.translate()
#if traducido2 == traducido:
# print("las secuencias se coinciden")

from Bio.SeqRecord import SeqRecord #para secuencias grandes
from Bio import SeqIO #para secuencias grandes
seqs= list(SeqIO.parse("CytBDNA.txt", "fasta"))
print(seqs[15])
for record in SeqIO.parse("CytBDNA.txt", "fasta"):
    if (record.description.split()[1] == "glycoprotein"):
        print(record.id)
#for R in SeqIO.parse ("CytBDNA.txt", "fasta"):
 #dna=SeqIO.parse(CytBDNA.txt, "fasta")
 #print(R.id, len(R.seq))
 #print(R.description)
 #print(R.seq.translate())
 