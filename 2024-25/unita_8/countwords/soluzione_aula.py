# apro il file
# creo un insieme vuoto
# per ogni riga del file
#   individua le parole
#   aggiungi le parole all'insieme
# conto il numero di elementi nell'insieme: è il numero di parole univoche
# chiudo il file

def main():
    file_name = input("Inserisci il nome del file da leggere: ")
    try:
        input_file = open(file_name, "r", encoding="utf-8")
        numero_parole = conta_parole_univoche(input_file)
        print(f"Il file contiene {numero_parole} parole univoche")
        input_file.close()
    except OSError:
        print(f"Il file {file_name} non esiste")


def conta_parole_univoche(input_file):
    insieme_parole = set()
    for riga in input_file:
        parole = riga.split()
        for parola in parole:
            parola_pulita = pulisci_parola(parola)
            insieme_parole.add(parola_pulita)
    
    return len(insieme_parole)


def pulisci_parola(parola):
    stringa = ""
    for carattere in parola:
        if carattere.isalpha():
            stringa = stringa + carattere.lower()
    
    return stringa


main()