# 1) stampo il file
# 2) memorizzo il file in una lista di dizionari
from csv import DictReader
from operator import itemgetter

def main():
    # apro il file
    # leggo una riga alla volta
    #   memorizzo la riga in un dizionario
    # ordino la lista di dizionari
    # chiudo il file
    try:
        inputfile = open("world_area_pop.csv", "r", encoding="utf-8")
        inputfile.readline()    # scarto l'intestazione del file
        lista = []
        for riga in inputfile:
            dizionario_nazione = costruisci_dizionario(riga)
            lista.append(dizionario_nazione)
        inputfile.close()

        # ordino la lista di dizionari sulla superficie
        lista_ordinata = sorted(lista, key=itemgetter("superficie"), reverse=True)
        #for elemento in lista_ordinata:
        #    print(f"Nazione: {elemento['nazione']}", end=" - ")
        #    print(f"superficie: {elemento['superficie']}", end=" - ")
        #    print(f"popolazione: {elemento['popolazione']}")

        # ordino la lista di dizionari sulla densita (abitanti/km^2)
        #lista_ordinata = sorted(lista, key=densita, reverse=True)
        lista_ordinata = sorted(lista, key=lambda elemento:1000 if elemento["superficie"] == 0 else elemento["popolazione"] / elemento["superficie"], reverse=True)
        for elemento in lista_ordinata:
            print(f"Nazione: {elemento['nazione']}", end=" - ")
            print(f"superficie: {elemento['superficie']}", end=" - ")
            print(f"popolazione: {elemento['popolazione']}")
            
    except OSError:
        print("Il file non esiste")

def densita(elemento):
    return 1000 if elemento["superficie"] == 0 else elemento["popolazione"] / elemento["superficie"]
    # equivalente a:
    #if elemento["superficie"] == 0:
    #    return 1000     # mia scelta
    #else:
    #    return elemento["popolazione"] / elemento["superficie"]

def main_con_dict_reader():
    # questo main usa il DictReader per leggere il file
    try:
        inputfile = open("world_area_pop.csv", "r", encoding="utf-8")
        csv_dict_reader = DictReader(inputfile)
        lista = []
        for elemento in csv_dict_reader:
            print(f"Nazione: {elemento['nazione']}", end=" - ")
            print(f"superficie: {elemento['superficie']}", end=" - ")
            print(f"popolazione: {elemento['popolazione']}")
            lista.append(elemento)
        inputfile.close()
    except OSError:
        print("Il file non esiste")

def main_prima_versione():
    # apro il file
    # leggo una riga alla volta
    #   memorizzo la riga in un dizionario
    #   stampo il dizionario
    # chiudo il file
    try:
        inputfile = open("world_area_pop.csv", "r", encoding="utf-8")
        inputfile.readline()    # scarto l'intestazione del file
        lista = []
        for riga in inputfile:
            dizionario_nazione = costruisci_dizionario(riga)
            print(f"Nazione: {dizionario_nazione['nazione']}", end=" - ")
            print(f"superficie: {dizionario_nazione['superficie']}", end=" - ")
            print(f"popolazione: {dizionario_nazione['popolazione']}")
            lista.append(dizionario_nazione)
        inputfile.close()
    except OSError:
        print("Il file non esiste")

def costruisci_dizionario(riga):
    campi = riga.rsplit(",", maxsplit=2)
    dizionario = dict()     # equivalente a dizionario = {}
    dizionario["nazione"] = campi[0]
    dizionario["superficie"] = int(campi[1])
    dizionario["popolazione"] = int(campi[2])

    # equivalente a:
    #dizionario = {"nazione": campi[0],
    #              "superficie": int(campi[1]),
    #              "popolazione": int(campi[2])}

    return dizionario

main()