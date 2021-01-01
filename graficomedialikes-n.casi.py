import csv
import re
import pandas as pd
import io
import requests
import matplotlib.pyplot as plt
import numpy as np
import csv
import pandas as pd
import pylab
import scipy
from scipy import stats, optimize, interpolate


with open('decessi.csv', encoding="utf8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    array2=[]
    arrayg=[]
    for linea in csv_reader:
        array2.append(int(linea[1]))
    mac = max(array2)
    mic = min(array2)
    ma=1
    for h in array2:
        if(h== mic):
            arrayg.append(0.0)
        else:
            x = (h * ma)/ mac
            arrayg.append(x)



with open('media_likes.csv', encoding="utf8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    array=[]
    array1=[]
    array6=[]
    for linea in csv_reader:
        array.append(linea[0])
        array1.append(float(linea[1]))
    mac = max(array1)
    mic = min(array1)
    ma=1
    for h in array1:
        if(h== mic):
            array6.append(0.0)
        else:
            x = (h * ma)/ mac
            array6.append(x)

#grafico media dei likes normalizzato e numero di casi per giorno
#data
x = np.array(array)
#mediadeilikes
y = np.array(array6)
#numero dei casi
t= np.array(arrayg)
#calcolo l'indice di pearson
print((scipy.stats. pearsonr(array6,arrayg)))

plt.xticks(rotation="vertical")

plt.plot(x, y, marker = ".", color = 'red', label="media likes normalizzato")
plt.plot(x, t, marker = ".", color = 'g', label=" numero di casi normalizzato ")
pylab.legend(loc='upper left')


plt.title("Relazione media likes e numero di casi")
plt.xlabel("data")
plt.ylabel("media score-medialikes")
plt.show()
