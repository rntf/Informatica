import zipfile
import csv
from matplotlib import pyplot

FILENAME = 'Informatica Corso 1.csv'

# Leggi l'elenco degli studenti e salvalo in un array
def leggi_file(nomeFile):
    with zipfile.ZipFile(nomeFile + '.zip', 'r') as zip_ref:
        zip_ref.extractall()
    file = open(nomeFile, 'r', encoding="utf-8")
    reader = csv.reader(file)
    primaRiga = True
    studenti = []
    for line in reader:
        if primaRiga:   # salta la prima riga (header)
            primaRiga = False
        else:
            studenti.append(line)
    file.close()
    return studenti

# Estrai i nomi di battesimo da un elenco di studenti
def estrai_nomi(elenco):
    lista_nomi = []
    for riga in elenco:
        lista_nomi.append(riga[1].strip().capitalize())
    return lista_nomi

# Calcola le frequenze dei vari nomi presenti in un array
def calcola_frequenze(tokens):
    freq = {}
    for token in tokens:
        if token in freq:
            freq[token] = freq[token] + 1
        else:
            freq[token] = 1
    return freq

# Calcola il massimo valore presente nelle frequenze
def max_frequenza(freq):
    return max(freq.values())

# Restituisce il nome che compare il numero di volte indicato
def nomi_piu_frequenti(freq, max):
    return [nome for (nome, frequenza) in freq.items() if frequenza == max]

def main():
    studenti = leggi_file(FILENAME)
    nomi = estrai_nomi(studenti)
    print(f"Nella classe ci sono {len(studenti)} studenti")
    frequenze = calcola_frequenze(nomi)
    max = max_frequenza(frequenze)
    print(f"Il nome più frequente compare {max} volte")
    nomiMax = nomi_piu_frequenti(frequenze, max)
    print(f"Si tratta di: {nomiMax}")
    # estrai solo i nomi che compaiono almeno 2 volte
    frequenze2 = {k:v for (k, v) in frequenze.items() if v >= 2}
    print(f"I nomi che compaiono più di una volta sono {', '.join(sorted(list(frequenze2.keys())))}.")

    pyplot.barh(list(frequenze2.keys()), frequenze2.values())
    pyplot.show()
    return

main()
