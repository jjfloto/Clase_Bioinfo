# Script para la traducción de secuencias nucleotídicas
#!/usr/bin/env python3
#librerías necesarias

#importar librerías
import os
import sys

import Bio
from Bio import SeqIO
from Bio.Seq import Seq
#output para almacenar las secuencias proteicas
output_file="prot_sal.fasta"
dnaAln="alineamientos.fasta"
# abrimos el archivo output para poder escribir en este
with open(output_file, "w") as out_handle:
 for record in SeqIO.parse(dnaAln, "fasta"):
        mARN=record.seq.transcribe()
        prot=mARN.translate()
        # Escribir la secuencia proteica en el archivo de salida en formato FASTA
        out_handle.write(f">{record.id}\n{prot}\n")
