#!/usr/bin/env python3
import Bio

from Bio.Seq import Seq
sec=Seq("ATATCGTGCGCGCTA")
transcrito= sec.transcribe()
traducido=sec.translate()
traducido2=transcrito.translate()
#if traducido2 == traducido:
 #print("las secuencias se coinciden")

from Bio.SeqRecord import SeqRecord #para secuencias grandes
from Bio import SeqIO #para secuencias grandes
seqs= list(SeqIO.parse("CytBDNA.txt", "fasta"))
#print(seqs[15])
#Este codigo es util para recorrer un archivo con multiples secuencias
# para obtener ADN, ARN, proteina.
for record in SeqIO.parse("CytBDNA.txt", "fasta"):
    mRNA= record.seq.transcribe()
    prot= mRNA.translate("Vertebrate Mitochondrial")
    ñao=record.id,prot
   