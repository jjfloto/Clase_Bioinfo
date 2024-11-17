#Objetivo que sea un script que cuente letras y lineas
#!/bin/bash/
for cuento in $(ls)
do
wc -m $cuento;
wc -l $cuento;
done

