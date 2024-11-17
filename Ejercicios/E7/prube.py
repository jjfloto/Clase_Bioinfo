import Bio
from Bio.SeqRecord import SeqRecord #para secuencias grandes
from Bio import SeqIO #para secuencias grandes
#(record for record in SeqIO.parse("Cytb.prot.fa", "fasta") if (record.description.split()[9] == "glycoprotein"))
for record in SeqIO.parse("Cytb.prot.fa", "fasta"):
	 i=1
	 if record.description.split()[i] == "glycoprotein":
	  print(record.description.split()[i],"concuerda")
	 else:
	  print("ñao ñao")
	 i=i+1
