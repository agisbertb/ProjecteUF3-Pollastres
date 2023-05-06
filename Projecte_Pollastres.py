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
xml = ""
num_pesades = 0
pesades = []


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

ahir()

def lot_fitxer(filename):
    global lot
    parts = filename.split("_")
    lot = parts[1].split(".")[0]
    return lot

def data_fitxer(filename):
    parts = filename.split("_")
    date = parts[0]
    return date

for file in get_files():
    if data_fitxer(file) == ahir():
        nom_valids.append(file)

def med():
    global mediana
    pesosvalids.sort()
    if len(pesosvalids) % 2 == 0:
        mediana = (pesosvalids[len(pesosvalids)//2] + pesosvalids[len(pesosvalids)//2-1])/2
    else:
        mediana = pesosvalids[len(pesosvalids)//2]
    mediana = str(mediana)
    mediana = mediana[0:7]
    mediana = float(mediana)
    return mediana

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

def generarXML(valor,etiqueta):
    return "<"+etiqueta+">"+str(valor)+"</"+etiqueta+">\n"

def generar():
    global total
    for file in nom_valids:
        lot = lot_fitxer(file)
        file = open('noprocessats/'+file, 'r')
        lines = file.readlines()
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
        global num_pesades
        num_pesades = 0
        global xml
        global pesades
        xml = ""
        total += len(lines)
        for line in lines:
            try:
                num_pesades = +1
                float(line)
                pesosvalids.append(float(line))
                pollos += float(line)
                if float(line) < float(config_vars[3]) or float(line) > float(config_vars[4]):
                    rangsino += 1
            except ValueError:
                invalid += 1
        valid = total - invalid
        mitjana = pollos/valid
        mitjana = str(mitjana)
        mitjana = mitjana[0:7]
        mitjana = float(mitjana)
        med()
        desv()
        xml = generarXML(valid,"num_animals")
        xml += generarXML(  mitjana,"mitja")
        xml += generarXML(mediana,"mediana")
        xml += generarXML(desviacio,"desviacio_tipica")
        xml = "<dades_animals>\n"+xml+"</dades_animals>\n"
        xml = generarXML(lot,   "lot")+generarXML(total,"num_pesades")+generarXML(invalid,"errors_pesada")+generarXML(rangsino,"fora_range")+xml
        xml = "<pesada>\n"+xml+"</pesada>\n"
        pesades.append(xml)

generar()

def pesades_xml():
    for pesada in pesades:
        animalsxml = open(parametres(2).rstrip()+"/"+str(data_fitxer(nom_valids[1]))+".xml","a")
        animalsxml.write(pesada)
        animalsxml.close()

pesades_xml()

def afegir_et_pesades():
    pesadesxml = open(parametres(2).rstrip()+"/"+str(data_fitxer(nom_valids[1]))+".xml","r")
    pesadesxml_lines = pesadesxml.readlines()
    pesadesxml.close()
    pesadesxml = open(parametres(2).rstrip()+"/"+str(data_fitxer(nom_valids[1]))+".xml","w")
    pesadesxml.write("<pesades>\n")
    pesadesxml.writelines(pesadesxml_lines)
    pesadesxml.write("</pesades>\n")
    pesadesxml.close()

afegir_et_pesades()

def mover():
    for file in nom_valids:
        Path('noprocessats/'+file).rename(parametres(1).rstrip()+"/"+file)

mover()


