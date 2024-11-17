#!/bin/bash
# script para automatizar descarga y procesamiento
#crear directorio
mkdir E4
#entrar en directorio
cd E4
#pasar los archivos
cp E2/CytBDNA.txt .
cp E3/CytBProt.txt .

cp culebra.py .
python3 culebra.py
