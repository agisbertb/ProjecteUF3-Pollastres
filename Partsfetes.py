#Comprovar el total de pesades que hi ha
#Comprovar si una entrada és vàlida o no
#Comprovar si una entrada està dins del rang de pes
#Comprovar la mitjana de les pesades
#Comprovar la mediana de les pesades
#Comprovar el total de pesades vàlides
#Calcular la desviació típica de les pesades vàlides
#Creacio de l'xml


import os
from pathlib import Path
from datetime import date
import math

config = open('config.txt', 'r')
config_vars=config.readlines()


file = open('noprocessats/20230421_01.txt', 'r')
lines = file.readlines()
global total
total = len(lines)
global valid 
valid = 0
global invalid
invalid = 0
global rangsino 
rangsino = 0
global mitjana
mitjana = 0
global pesosvalids
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
        
valid = total - invalid
valid = valid - rangsino

mitjana = str(mitjana)
mitjana = mitjana[0:7]
mitjana = float(mitjana)


pesosvalids.sort()
if len(pesosvalids) % 2 == 0:
    mediana = (pesosvalids[len(pesosvalids)//2] + pesosvalids[len(pesosvalids)//2-1])/2
else:
    mediana = pesosvalids[len(pesosvalids)//2]


sum = 0
for i in range(len(pesosvalids)):
    sum += (pesosvalids[i] - mitjana)**2
sum = sum / len(pesosvalids)
sum = math.sqrt(sum)

sum = str(sum)
sum = sum[0:5]
sum = float(sum)



'''
print("num_animals: ", valid)
print("Error de pesades: ", invalid)
print("Fora de rang: ", rangsino)
print("Num_pesades", total)
print("Mitjana: ", mitjana)
print("Desviacio tipica: ", sum)
print("Mediana: ", mediana)
'''

resultat = open('resultat.xml', 'w')

#Añadir etiquetas al xml
resultat.write("<pesades>\n")
resultat.write("    <pesada>\n")
resultat.write ("       <lot>"+str("0")+"</lot>\n")
resultat.write ("       <num_pesada>"+str(total)+"</num_pesada>\n") 
resultat.write ("       <errors>"+str(invalid)+"</errors>\n")
resultat.write ("       <fora_rang>"+str(rangsino)+"</fora_rang>\n")

resultat.write ("       <dades_animals>\n")
resultat.write ("           <num_animals>"+str(valid)+"</num_animals>\n")
resultat.write ("           <mitjana>"+str(mitjana)+"</mitjana>\n")
resultat.write ("           <mediana>"+str(mediana)+"</mediana>\n")
resultat.write ("           <desviacio_tipica>"+str(sum)+"</desviacio_tipica>\n")
resultat.write ("       </dades_animals>\n")
resultat.write("    </pesada>\n")
resultat.write("</pesades>\n")
resultat.close()