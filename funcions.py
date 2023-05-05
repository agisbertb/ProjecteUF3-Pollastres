import os
from pathlib import Path
from datetime import *
import math
files = []
lot = 0
total = 0
valid = 0
invalid = 0
rangsino = 0
mitjana = 0
pesosvalids = []
desviacio = 0
sum = 0
mediana = 0
nom_valids = []


config = open('config.txt', 'r')
config_vars = config.readlines()
config.close()

def parametres(num):
    return str(config_vars[num])

#Lista de archivos en el directorio no processats
def get_files():
    global files
    for file in os.listdir(parametres(0).rstrip()):
        if file.endswith(".txt"):
            files.append(file)
    return files

def ahir():
    today = date.today()
    yesterday = today - timedelta(days = 1)
    return yesterday.strftime("%Y%m%d")

def lot_fitxer(filename):
    global lot
    parts = filename.split("_")
    lot = parts[1].split(".")[0]
    return lot


def data_fitxer(filename):
    parts = filename.split("_")
    date = parts[0]
    return date

#Comprobar si el archivo es de ayer
def comprobar(files):
    for file in files:
        if data_fitxer(file) == ahir():
            global nom_valids
            nom_valids.append(file)
            lot = lot_fitxer(file)
            file = open('noprocessats/'+file, 'r')
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
            pollos = 0
            for line in lines:
                try:
                    float(line)
                    valid += 1
                    pesosvalids.append(float(line))
                    pollos += float(line)
                    if float(line) < float(config_vars[3]) or float(line) > float(config_vars[4]):
                        rangsino += 1
                except ValueError:
                    invalid += 1
            mitjana = pollos/valid
            mitjana = str(mitjana)
            mitjana = mitjana[0:7]
            mitjana = float(mitjana)
comprobar(get_files())

def med():
    global mediana
    pesosvalids.sort()
    if len(pesosvalids) % 2 == 0:
        mediana = (pesosvalids[len(pesosvalids)//2] + pesosvalids[len(pesosvalids)//2-1])/2
    else:
        mediana = pesosvalids[len(pesosvalids)//2]
    return mediana

med()

def desv():
    global sum
    global desviacio
    sum = 0
    for i in pesosvalids:
        sum += (i - mitjana)**2
    desviacio = math.sqrt(sum/total)
    desviacio = str(desviacio)
    desviacio = desviacio[0:7]
    desviacio = float(desviacio)
    return desviacio

desv()

print("nom_valids: "+str(nom_valids))
print("lot: "+str(lot))
print("num_pesades: "+str(total))
print("errors_pesada: "+str(invalid))
print("fora_range: "+str(rangsino))
print("mitja: "+str(mitjana))
print("mediana: "+str(mediana))
print("desviacio_tipica: "+str(desviacio))

def generarXML(valor,etiqueta):
    return "<"+etiqueta+">"+str(valor)+"</"+etiqueta+">\n"


def xml():
    global xml
    xml = ""
    xml = generarXML(1,"num_animal")
    xml += generarXML(1.2,"mitja")
    xml += generarXML(1.3,"mediana")
    xml += generarXML(0.1,"desviacio_tipica")
    xml = "<dades_animals>\n"+xml+"</dades_animals>\n"
    xml = generarXML(1,"lot")+generarXML(3,"num_pesades")+generarXML(0,"errors_pesada")+generarXML(0,"fora_range")+xml
    xml = "<pesada>\n"+xml+"</pesada>\n"
    animalsXML = open("animals.xml","w")
    animalsXML.write(xml)
    animalsXML.close()
    print(xml)
 
print(parametres(2).rstrip()+".xml")

