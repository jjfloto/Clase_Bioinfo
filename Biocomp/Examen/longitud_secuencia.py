#!/usr/bin/env python3
#el siguiente script se crea para dar solucion a los puntos 1 al 5
#librerias 
import Bio
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
#definiendo variable
DNA_ecoli_secuence="Ecoli_phoA.fasta"

#funcion para leer la longitud
for R in SeqIO.parse(DNA_ecoli_secuence, "fasta"):
 print("la longitud de nucleotidos del organismo es:", len(R.seq))

#Contar posiciones hasta hallar el codon "AUG"
codon_inicio="AUG"
contador=0
ecoli_z=SeqIO.read("Ecoli_phoA.fasta", "fasta")
ecoli_seq=ecoli_z.seq
ecoli_trancrip=ecoli_seq.transcribe()
for i in range(len(ecoli_trancrip)):
    if ecoli_trancrip[i:i+3] == codon_inicio:
        print('codon de inicio AUG inicia en', i)
        break
else:
    print("no se encontro")
# obteniendo el CDS
print("tamaño del traducido completo en nucleotidos es:", len(ecoli_trancrip))
print("region CDS")
#print(ecoli_trancrip[75:1500])
#Nota falto colocar la parte traducida
ecoli_traducida=ecoli_trancrip.translate()
print("el traducido es:", ecoli_traducida)
print("el CDS tiene un tamaño de nc:" ,len(ecoli_trancrip[75:1500]))
