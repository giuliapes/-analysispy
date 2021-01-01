import csv
import math
import re
import sys
import re
from csv import writer
import matplotlib.pylab as plt
import numpy as np
import csv
import pandas as pd
#calcolo la media dei likes per giorno
dictionary = {}
with open('provasentiment.csv', encoding="utf8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    for linea in csv_reader:
        regExp = re.findall(r'\d\d\d\d[-/]\d\d[-/]\d\d',linea[4])
        if regExp[0] in dictionary:
            dictionary[regExp[0]].append(linea[2])
        else:
            dictionary[regExp[0]]=[]
            dictionary[regExp[0]].append(linea[2])

array=[]
s = 0
for k in dictionary['2020-10-13']:
    s+=float(k )

for i in dictionary:
    somma = 0
    lunghezza = len(dictionary[i])
    for j in dictionary[i]:

        somma+=float(j)
    print(i +","+str(somma/lunghezza))
