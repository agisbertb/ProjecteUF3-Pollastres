#Comprovar el total de pesades que hi ha
#Comprovar si una entrada és vàlida o no
#Comprovar si una entrada està dins del rang de pes
#Comprovar la mitjana de les pesades
#Comprovar la mediana de les pesades
#Comprovar el total de pesades vàlides

import os
from pathlib import Path
from datetime import date

config = open('config.txt', 'r')
config_vars=config.readlines()

file = open('noprocessats/20230421_01.txt', 'r')
lines = file.readlines()
total = len(lines)
valid = 0
invalid = 0
rangsino = 0
mitjana = 0
pesosvalids = []
for line in lines:
    try:
        float(line)
        valid += 1
        pesosvalids.append(float(line))
        mitjana += float(line)
        mitjana = mitjana/total
        if float(line) < float(config_vars[3]) or float(line) > float(config_vars[4]):
            rangsino += 1
    except ValueError:
        invalid += 1

print("num_animals: ", valid)
print("Error de pesades: ", invalid)
print("Fora de rang: ", rangsino)
print("Num_pesades", total)
print("Mitjana: ", mitjana)

#Mediana
pesosvalids.sort()
if len(pesosvalids) % 2 == 0:
    mediana = (pesosvalids[len(pesosvalids)//2] + pesosvalids[len(pesosvalids)//2-1])/2
else:
    mediana = pesosvalids[len(pesosvalids)//2]
print("Mediana: ", mediana)
