#numero decessi al giorno
import csv
import re
import pandas as pd
import io
import requests
import matplotlib.pyplot as plt
import numpy as np

    #print(array2)


with open('andamento-nazionale.csv', encoding="utf8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    v=0
    array=[]
    for linea in csv_reader:
        print(linea[0]+','+str(int(linea[10])-v))
        v=int(linea[10])



        #print(linea[0])
        #for i in linea:




#    for i in [linea[9]]:
#        if i=="2":
#            print("trovato")
#        else:
#            print("non trov")
#for linea in csv_reader:
    #print(linea[0])

#    print(linea)

#print(f.text)
#print(testo)
#for row in testo:
    #print(testo[11])

#for linea in testo:
#    a=linea[10]
#    print(a)R

#    print(testo[0])

#numero di casi giornalieri
