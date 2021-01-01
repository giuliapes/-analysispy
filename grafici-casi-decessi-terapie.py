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
import pylab
import scipy
from scipy import stats, optimize, interpolate
from statistics import *

dictionary = {}

with open('provasentiment.csv', encoding="utf8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    for linea in csv_reader:
        regExp = re.findall(r'\d\d\d\d[-/]\d\d[-/]\d\d',linea[4])
        if regExp[0] in dictionary:
            dictionary[regExp[0]].append(linea[0])
        else:
            dictionary[regExp[0]]=[]
            dictionary[regExp[0]].append(linea[0])

#print(dictionary['2020-10-13'])
array1=[]
array2=[]
array3=[]
array4=[]
arrayj=[]
g=[]
a=0
for i in dictionary:
    neg = 0
    pos = 0
    neutr = 0
    lung = len(dictionary[i])
    for j in dictionary[i]:
        if(float(j)<0):
            neg = neg + 1
        elif(float(j)>0):
            pos = pos + 1
        elif(float(j)==0):
            neutr = neutr + 1
#    print('Indice negatività per la data '+ i+': '+ str(neg/lung))
#    print('Indice positività per la data '+ i+': '+ str(pos/lung))
#    print('Indice neutralità per la data '+ i+': '+ str(neutr/lung))

    a=(neg/lung)
    b=(pos/lung)
    c=(neutr/lung)
#data
    array1.append(i)
#negatività
    array2.append(a)
#positività
    array3.append(b)
#neutralità
    array4.append(c)
#apro il file csv casi giorno dove sono salvati il numero di casi per giorno ricavati dal sito della protezione civile e poi sottratti
#da numerocasi.py
with open('numerocasi.csv', encoding="utf8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    #print(linea[13])
    array5=[]
    arrayg=[]

    for linea in csv_reader:
        array5.append(int(linea[1]))
    #normalizzo i dati
    mac = max(array5)
    mic = min(array5)
    ma=1
    for h in array5:
        if(h== mic):
            arrayg.append(0.0)
        else:
            x = (h * ma)/ mac
            arrayg.append(x)
#decessi
#apro il file csv casi giorno dove sono salvati il numero di casi per giorno ricavati dal sito della protezione civile e poi sottratti
#da decessi.py
with open('decessi.csv', encoding="utf8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    array6=[]
    arrays=[]
    for linea in csv_reader:
        array6.append(int(linea[1]))
    #normalizzo i dati
    mac = max(array6)
    mic = min(array6)
    ma = 1
    for h in array6:
        if(h== mic):
            arrays.append(0.0)
        else:
            x = (h * ma)/ mac
            arrays.append(x)



#terapie intensive
#apro il file csv casi giorno dove sono salvati il numero di casi per giorno ricavati dal sito della protezione civile e poi sottratti
#da terapie.py
with open('terapie.csv', encoding="utf8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    #print(linea[13])
    array10=[]
    arraye=[]
    for linea in csv_reader:
        array10.append(int(linea[1]))
    #normalizzo i dati
    mac = max(array10)
    mic= min(array6)
    ma=1
    for h in array10:
        if(h==mic):
            arraye.append(0.0)
        else:
            x= (h*ma)/mac
            arraye.append(x)

#grafico indice positività e numero casi al giorno
#data
x = np.array(array1)
#neg
#neg = np.array(array2)
#pos
p= np.array(array3)
#neutralità
#n= np.array(array4)
casi=np.array(arrayg)
#calcolare indice di pearson
#print((scipy.stats. pearsonr(p,casi)))

#scritte verticali per la data
plt.xticks(rotation="vertical")

#plt.plot(x, neg, marker = ".", color = 'red', label='indice negatività')
plt.plot(x, p, marker = ".", color = 'g', label='indice positività')
#plt.plot(x, n, marker = ".", color = 'yellow', label='indice neutralità')
plt.plot(x, casi, marker = ".", color = 'blue', label='casi al giorno')

pylab.legend(loc='lower left')
pylab.ylim(-0.3, 1.2)
plt.title("Relazione tra Indice di positività e numero casi")
plt.xlabel("data")
plt.ylabel("Indice di positività e il numero di casi al giorno")
plt.show()
#print((scipy.stats.pearsonr(arrayg,p)))

#grafico tra indice di positività e i decessi
decessi= np.array(arrays)
#scritte verticali per la data
plt.xticks(rotation="vertical")
#y2= np.array(array2)
#plt.plot(x, neg, marker = ".", color = 'red', label='indice negatività')
plt.plot(x, p, marker = ".", color = 'g', label='indice positività')
#plt.plot(x, n, marker = ".", color = 'yellow', label='indice neutralità')
plt.plot(x, decessi, marker = ".", color = 'blue', label='decessi al giorno')

pylab.legend(loc='lower right')
pylab.ylim(-0.6, 1.2)
plt.title("Relazione tra Indice di positività e numero di decessi al giorno")
plt.xlabel("data")
plt.ylabel("Indici di positività e decessi")
plt.show()
#print((scipy.stats.pearsonr(arrays,p)))


#grafico indice di positività e terapie intensive
terapie= np.array(arraye)
#scritte verticali per le date
plt.xticks(rotation="vertical")

#plt.plot(x, neg, marker = ".", color = 'red', label='indice negatività')
plt.plot(x, p, marker = ".", color = 'g', label='indice positività')
#plt.plot(x, n, marker = ".", color = 'yellow', label='indice neutralità')
plt.plot(x, terapie, marker = ".", color = 'blue', label='ingressi nelle terapie intensive')

pylab.legend(loc='lower left')
pylab.ylim(-0.6, 1.2)
plt.title("Relazione tra Indice di positività e ingressi nelle terapie intensive al giorno")
plt.xlabel("data")
plt.ylabel("Indice di positività e ingressi nelle terapie intensive")
plt.show()
#print((scipy.stats.pearsonr(arraye,p)))
