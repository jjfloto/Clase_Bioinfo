#ejecutamos el culebra
python3 script_procesamiento.py
dna="CytBDNA"
prot="CytBProt"
 print("procesamiento de secuencias ADN")
 from Bio import SeqIO
 for R in SeqIO.parse(dna, "fasta"):
  print("el id es", R.id, "con un # de nc", len(R.seq))
  mRNA=R.seq.transcribe()
  proteins=mRNA.translate(table="Vertebrate Mitochondrial")
  print("id de mRNA", R.id)
  print("id de proteina", R.id)
print("procesado de proteinas")
 for R in SeqIO.parse(prot, "fasta"):
  print("el id es", R.id, "con un # de a.a", len(R.seq))
#ahora hacemos el filtrador de proteinas con mas de 100a.a
filtrador=[]
 for R in SeqIO.parse(prot, "fasta"):
  if len(R.seq) > 100:
   filtrador.append(R)
   #print("id del organismo", R.id, "tamaño a.a", len(R.seq))
output="proteinas filtradas.fasta"
SeqIO.write(filtrador, output, "fasta")
print(f"secuencias de proteinas filtradas guardadas en {output}")
