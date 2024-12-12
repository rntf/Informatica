# apro il file
# creo un insieme vuoto
# per ogni riga del file
#   individua le parole
#   aggiungi le parole all'insieme
# conto il numero di elementi nell'insieme: è il numero di parole univoche
# chiudo il file

#from datetime import datetime
import time

def main():
    file_name = input("Inserisci il nome del file da leggere: ")
    try:
        input_file = open(file_name, "r", encoding="utf-8")
        inizio = time.time()
        insieme_parole = estrai_parole(input_file)
        fine = time.time()
        print(f"Il file contiene {len(insieme_parole)} parole univoche")
        print(f"tempo di esecuzione: {fine - inizio}")
        input_file.close()
    except OSError:
        print(f"Il file {file_name} non esiste")


def estrai_parole(input_file):
    insieme_parole = set()
    for riga in input_file:
        parole = riga.split()
        for parola in parole:
            parola_pulita = pulisci_parola(parola)
            insieme_parole.add(parola_pulita)
    
    return insieme_parole


def estrai_parole2(input_file):
    # molto più lenta della funzione con l'insieme
    lista_parole = []
    for riga in input_file:
        parole = riga.split()
        for parola in parole:
            parola_pulita = pulisci_parola(parola)
            if parola_pulita not in lista_parole:
                lista_parole.append(parola_pulita)
    
    return lista_parole


def pulisci_parola(parola):
    stringa = ""
    for carattere in parola:
        if carattere.isalpha():
            stringa = stringa + carattere.lower()
    
    return stringa


main()