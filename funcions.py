import os
from pathlib import Path
from datetime import date
import math

def data_file_ayer():
    ayer = date.today()
    ayer = ayer.strftime("%Y%m%d")
    ayer = int(ayer)
    ayer = ayer - 1
    return ayer
print(data_file_ayer())

def get_file_number(filename):
    parts = filename.split("_")
    lot = parts[1].split(".")[0]
    return lot
print(get_file_number("20230421_01.txt"))


def get_file_date(filename):
    parts = filename.split("_")
    date = parts[0]
    return date
print(get_file_date("20230421_01.txt"))

