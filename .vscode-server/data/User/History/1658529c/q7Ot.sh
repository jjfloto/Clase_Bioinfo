#!/usr/bin/env python3
#librerias necesarias

#importar librerias
import os
import sys

import Bio
from Bio import SeqIO
from Bio.Seq import Seq
#output para almacenar las secuencias proteicas
output_file="prot_sal.fasta"
dnaAln="unido.txt"
for record in SeqIO.parse(dnaAln, "fasta"):
        mARN=record.seq.transcribe()
        prot=mARN.translate()
        echo prot >> "$output_file"
