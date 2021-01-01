#numero terapie al giorno
import csv
import re
import pandas as pd
import io
import requests
import matplotlib.pyplot as plt
import numpy as np
#apro il file della protezione civile e salvo in un csv il numero di casi giornalieri per le terapie intensive 
with open('andamento-nazionale.csv', encoding="utf8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    v=0
    array=[]
    for linea in csv_reader:
        print(linea[0]+','+str(int(linea[3])-v))
        v=int(linea[3])
