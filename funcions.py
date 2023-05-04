import os
from pathlib import Path
from datetime import *


def data_file():
    today = datetime.date.today()
    yesterday = today - datetime.timedelta(days=1)
    yesterday_str = yesterday.strftime("%Y%m%d")
    return yesterday_str
print(data_file())

def get_file_number(filename):
    global lot
    parts = filename.split("_")
    lot = parts[1].split(".")[0]
    return lot
print(get_file_number("20230421_01.txt"))


def get_file_date(filename):
    parts = filename.split("_")
    date = parts[0]
    return date
print(get_file_date("20230421_01.txt"))
