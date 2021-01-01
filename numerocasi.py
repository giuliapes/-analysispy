#esempio due febbraio 2020
#il numero di casi quelli di oggi meno quello di ieri
#fare un grafico mettendo a confronto numero di casi con sentiment medio
#leggere dati dal sito

import csv
import re
import pandas as pd
import io
import requests
#csv_file='https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-andamento-nazionale/dpc-covid19-ita-andamento-nazionale.csv'
#f = requests.get(csv_file)

#print(f.text)

with open('andamento-nazionale.csv', encoding="utf8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    v=0

    for linea in csv_reader:
        print(linea[0]+','+str(int(linea[13])-v))
        v=int(linea[13])



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
