import os
from pathlib import Path
from datetime import date
import math

files = []



#Sacar todos los archivos de la carpeta noprocessats
def get_files():
    for file in os.listdir("noprocessats"):
        if file.endswith(".txt"):
            files.append(file)
    return files

#Fecha de hoy
def get_date():
    today = date.today()
    today = today.strftime("%Y%m%d")
    return today
#print(get_date())

def get_file_number(filename):
    parts = filename.split("_")
    number = parts[1].split(".")[0]
    return number
#print(get_file_number("20230421_01.txt"))

def get_file_date(filename):
    parts = filename.split("_")
    date = parts[0]
    return date
#print(get_file_date("20230421_01.txt"))

#Fecha y numero de cada archivo de la lista files
def get_file_date_and_number(files):
    global dates
    dates = []
    for file in files:
        date = get_file_date(file)
        number = get_file_number(file)
        dates.append(date)
        dates.append(number)
    return dates

get_files()
print(get_file_date_and_number(files))
