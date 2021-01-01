import csv
import math
import re
import sys
import re
import matplotlib.pylab as plt
import numpy as np
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
arrayl=[]
arrayg=[]
arraye=[]
arraymedia=[]
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
#inserisco i tre indici nell'arrayj
    arrayj.append(a)
    arrayj.append(b)
    arrayj.append(c)
#la media degli indici
    arraymedia.append(mean(arrayj))


#grafico indice positivtà e numero casi al giorno
#data
x = np.array(array1)
#neg
neg = np.array(array2)
#pos
p= np.array(array3)
#media degli indici
media=np.array(arraymedia)
#data in verticale
plt.xticks(rotation="vertical")

#plt.plot(x, neg, marker = ".", color = 'red', label='indice negatività')
plt.plot(x, p, marker = ".", color = 'g', label='indice positività')
#plt.plot(x, n, marker = ".", color = 'yellow', label='indice neutralità')
plt.plot(x,media, marker = ".", color = 'yellow', label='media indici')

pylab.legend(loc='lower left')
pylab.ylim(0.0, 1.2)
plt.title("Media indici e indice di positività")
plt.xlabel("data")
plt.ylabel("Media indici e indice di positività")
plt.show()
#deviazione standard indice positività
print(np.std(array3, axis = None))

#data in verticale
plt.xticks(rotation="vertical")

plt.plot(x, neg, marker = ".", color = 'red', label='indice negatività')
#plt.plot(x, p, marker = ".", color = 'g', label='indice positività')
#plt.plot(x, n, marker = ".", color = 'yellow', label='indice neutralità')
plt.plot(x,media, marker = ".", color = 'yellow', label='media indici')

pylab.legend(loc='lower left')
pylab.ylim(-0.3, 1.2)
plt.title("Media indici e indice di negatività")
plt.xlabel("data")
plt.ylabel("Media indici e indice di negatività")
plt.show()
#deviazione standard indice negatività
print(np.std(array2, axis = None))
