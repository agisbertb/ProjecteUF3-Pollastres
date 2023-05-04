import os
from pathlib import Path
from datetime import *
import math
files = []
lot = 0
config = open('config.txt', 'r')
config_vars = config.readlines()

#Lista de archivos en el directorio no processats
def get_files():
    global files
    for file in os.listdir("noprocessats"):
        if file.endswith(".txt"):
            files.append(file)
    return files

#Data d'ahir
def ahir():
    today = date.today()
    yesterday = today - timedelta(days = 1)
    return yesterday.strftime("%Y%m%d")
print(ahir())

def get_file_number(filename):
    global lot
    parts = filename.split("_")
    lot = parts[1].split(".")[0]
    return lot

def get_file_date(filename):
    parts = filename.split("_")
    date = parts[0]
    return date





  