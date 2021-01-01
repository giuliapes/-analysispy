#numero casi al giorno dal csv della protezione civile chiamato andamento-nazionale.csv
import csv
import re
import pandas as pd
import io
import requests

with open('andamento-nazionale.csv', encoding="utf8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    v=0
    for linea in csv_reader:
        print(linea[0]+','+str(int(linea[13])-v))
        v=int(linea[13])
