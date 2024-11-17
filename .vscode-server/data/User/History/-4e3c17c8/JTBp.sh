#!/bin/bash/
# Script para unir todos los archivos .txt en un solo archivo
output_file="unido.fasta"
# Crear archivo de salida o lo eliminamos para empezar desde cero
if [ -f "$output_file" ]; then
    rm "$output_file"
fi
for file in *.fasta
do
    # Verificamos que realmente existan archivos .fasta
    if [ -f "$file" ]; then
        echo "Uniendo el archivo: $file"
        cat "$file" >> "$output_file"
    fi
done

echo "Archivos unidos en $output_file"
#clustalw -infile=CytBProt.txt -type=nucleotide -output=phylip
