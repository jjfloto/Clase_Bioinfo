#!/usr/local/bin/python3

#importar librerias
import os
import sys

import Bio
from Bio import SeqIO
from Bio.Seq import Seq

dnaC="CytBDNA.txt"
for record in SeqIO.parse(dnaC, "fasta"):
	mARN=record.seq.transcribe()
	prot=mARN.translate(table="Vertebrate Mitochondrial")
	print(prot)
