#!/usr/bin/env python3

# Script por Laura Salazar Jaramillo
# Genera un subconjunto de glicoproteinas de SARS-covid 19

# Importamos las librerías necesarias
import os
import sys

import Bio
from Bio import SeqIO
from Bio.Seq import Seq

# Archivos de entrada (inputs)
dna_file = "Sars_cov.dna.fa"
prot_file = "Sars_cov.prot.fa"

# Listamos el tamano del genoma
for record in SeqIO.parse(dna_file, "fasta"):
    print("La longitud en nc del genoma es:", len(record.seq))

# Listamos los id y longitudes de las proteínas
for record in SeqIO.parse(prot_file, "fasta"):
    print(record.id, len(record.seq), record.description.split()[9])

# Seleccionamos las glicoproteínas y las guardamos en un archivo aparte
glycoproteins = (record for record in SeqIO.parse(prot_file, "fasta") if (record.description.split()[9] == "glycoprotein"))
SeqIO.write(glycoproteins, "sars_covid19_glycoproteins.fa", "fasta")
