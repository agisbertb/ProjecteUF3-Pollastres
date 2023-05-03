import os
from pathlib import Path
from datetime import date
'''
No processats txt: noprocessats/
Processats txt: processats/
generats xml: generats/
Pes minim: 1.5
Pes maxim: 4.0
Data: 2023/04/21

today = date.today()
d1 = today.strftime("%d/%m/%Y")
print("Avui es: ", d1)
'''
config = open('config.txt', 'r')
config_vars=config.readlines()

#Contar lineas del archivo anterior
#file = open('noprocessats/20230421_01.txt', 'r')
#print(len(file.readlines()))
'''''
#Contar lineas del archivo anterior pero contando a parte las lineas que no son numeros i si estan dentro del rango de max i min
file = open('noprocessats/20230421_01.txt', 'r')
lines = file.readlines()
total = len(lines)
valid = 0
invalid = 0
rangsino = 0
for line in lines:
    try:
        float(line)
        valid += 1
        if float(line) < float(config_vars[3]) or float(line) > float(config_vars[4]):
            rangsino += 1
    except ValueError:
        invalid += 1

print("Valid lines: ", valid)
print("Invalid lines: ", invalid)
print("Lines out of range: ", rangsino)
print("Total lines: ", total)

#Mitjana dels pesos del archivo anterior
file = open('noprocessats/20230421_01.txt', 'r')
lines = file.readlines()
total = len(lines)
valid = 0
invalid = 0
rangsino = 0
mitjana = 0
for line in lines:
    try:
        float(line)
        valid += 1
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
'''


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

#Coger 4 digitos de la mitjana
mitjana = str(mitjana)
mitjana = mitjana[0:7]
mitjana = float(mitjana)




#Mediana
pesosvalids.sort()
if len(pesosvalids) % 2 == 0:
    mediana = (pesosvalids[len(pesosvalids)//2] + pesosvalids[len(pesosvalids)//2-1])/2
else:
    mediana = pesosvalids[len(pesosvalids)//2]

#Desviacion tipica
import math
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















