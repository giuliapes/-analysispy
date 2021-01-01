import csv
from csv import writer
import re
import operator
import os
os.environ["PYTHONIOENCODING"] = "utf-8"
tweets = []

#rimuovere i caratteri ASCII
def strip_non_ascii(string):
    ''' Returns the string without non ASCII characters'''
    stripped = (c for c in string if 0 < ord(c) < 127)
    return ''.join(stripped)

#apro il file csv dati con le colonne descrizione, likes, retweets, data
with open('dati.csv', newline='', encoding='utf-8',errors='ignore') as csvfile: #cambia qui il nome del file
    reader = csv.reader(csvfile, delimiter=';')
    next(reader)

    for row in reader:

        tweet= dict()
        tweet['descrizione'] = row[0]
        tweet['likes'] = (int(row[1]))
        tweet['retweets'] = row[2]
        tweet['data'] = row[3]


#pulizia della descrizione
        # Ignora i retweets nella sezione descrizione
        if re.match(r'^RT.*', tweet['descrizione']):
            continue

        tweet['clean'] = tweet['descrizione']

        # Normalizza il caso
        tweet['clean'] = tweet['clean'].lower()

        # Rimuove gli # nella sezione clean
        tweet['clean'] = tweet['clean'].replace(r'#', '')


        # Remove multiple vowels symbol

        tweet['clean'] = re.sub(r'a+', 'a', tweet['clean'], flags=re.IGNORECASE)
        tweet['clean'] = re.sub(r'e+', 'e', tweet['clean'], flags=re.IGNORECASE)
        tweet['clean'] = re.sub(r'i+', 'i', tweet['clean'], flags=re.IGNORECASE)
        tweet['clean'] = re.sub(r'o+', 'o', tweet['clean'], flags=re.IGNORECASE)
        tweet['clean'] = re.sub(r'u+', 'u', tweet['clean'], flags=re.IGNORECASE)
        tweet['clean'] = re.sub(r'y+', 'y', tweet['clean'], flags=re.IGNORECASE)

        tweets.append(tweet)


# Crea una struttura dati per contenere il lessico.
# Useremo una dizione Python. La chiave del dizionario sarà la parola
# e il valore sarà il punteggio della parola.
lexicon = dict()

# Read in the lexicon.
with open('MAL.tsv', newline='', encoding='utf-8') as csvfile: #cambia qui il nome del file con il lessico
    reader = csv.reader(csvfile, delimiter='\t')
    for row in reader:
        lexicon[row[0]] = float(row[1])

#usa il lessico per il punteggio dei tweet
for tweet in tweets:
    score = 0
    for word in tweet['clean'].split():
        if word in lexicon:
            score = score + lexicon[word]

    tweet['score'] = score
    if (score > 0):
        tweet['sentiment'] = 'positive'
    elif (score < 0):
        tweet['sentiment'] = 'negative'
    else:
        tweet['sentiment'] = 'neutral'


#Stampa le statistiche di riepilogo
total = float(len(tweets))
num_pos = sum([1 for t in tweets if t['sentiment'] == 'positive'])
num_neg = sum([1 for t in tweets if t['sentiment'] == 'negative'])
num_neu = sum([1 for t in tweets if t['sentiment'] == 'neutral'])
print ("Positive: %5d (%.1f%%)" % (num_pos, 100.0 * (num_pos/total)))
print ("Negative: %5d (%.1f%%)" % (num_neg, 100.0 * (num_neg/total)))
print ("Neutral:  %5d (%.1f%%)" % (num_neu, 100.0 * (num_neu/total)))

# funzione per inserire in coda al file csv una lista di elementi
def appendiInCsv(file_name, list_of_elem):
    # Apre il file in modalità append, in modo che si possa scrivere in coda al contenuto del file
    with open(file_name, 'a+', newline='') as write_obj:
        #  Crea un oggetto writer dal modulo csv
        csv_writer = writer(write_obj,delimiter=';')
        # Aggiunge il contenuto dell'elenco come ultima riga nel file csv
        csv_writer.writerow(list_of_elem)

# Stampo e salvo in un file csv chiamato provasentiment.csv i dati trovati score, clean, likes, descrizione e data
tweets_sorted = sorted(tweets, key=lambda k: k['score'])
list_csv = ["score", "clean", "likes","descrizione", "data"]
appendiInCsv('provasentiment.csv',list_csv)
print ("\n\nTOP NEGATIVE TWEETS")
negative_tweets = [d for d in tweets_sorted if d['sentiment'] == 'negative']
for tweet in negative_tweets[0:]:
    print("score=%.2f, clean=%s, likes=%d, descrizione=%s, data=%s" % (tweet['score'], tweet['clean'],tweet['likes'], tweet['descrizione'], tweet['data']))
    a =[tweet['score'], tweet['clean'],tweet['likes'], tweet['descrizione'], tweet['data']]
    appendiInCsv("provasentiment.csv",a)
print ("\n\nTOP POSITIVE TWEETS")
positive_tweets = [d for d in tweets_sorted if d['sentiment'] == 'positive']
for tweet in positive_tweets[0:]:
    print("score=%.2f, clean= %s, likes=%d, descrizione=%s, data=%s" % (tweet['score'], tweet['clean'],tweet['likes'], tweet['descrizione'], tweet['data']))
    b=[tweet['score'], tweet['clean'],tweet['likes'], tweet['descrizione'], tweet['data']]
    appendiInCsv("provasentiment.csv",b)
print ("\n\nTOP NEUTRAL TWEETS")
neutral_tweets = [d for d in tweets_sorted if d['sentiment'] == 'neutral']
for tweet in neutral_tweets[0:]:
    print("score=%.2f, clean= %s, likes= %d, descrizione=%s, data=%s" % (tweet['score'], tweet['clean'],tweet['likes'], tweet['descrizione'], tweet['data']))
    c=[tweet['score'], tweet['clean'],tweet['likes'], tweet['descrizione'], tweet['data']]
    appendiInCsv("provasentiment.csv",c)
