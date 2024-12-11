FILENAME = 'world_area_pop.csv'

# 1) Lettura di una riga alla volta
try:
    file = open(FILENAME, 'r')

    nazioni = []
    prima = True

    for line in file:
        if not prima:
            record = line.rsplit(',', 2)
            nazioni.append({
                'nome': record[0],
                'area': int(record[1]),
                'popolazione': int(record[2])
            })
        else:
            prima = False # la prima linea contiene i nomi dei campi
    file.close()
except FileNotFoundError:
    print("Errore nell'apertura del file")


# 2) Lettura con DictReader
import csv

try:
    file = open(FILENAME, 'r')
    reader = csv.DictReader(file)

    nazioni = []
    for record in reader:
        nazioni.append(record)
    # oppure, più brevemente:
    # nazioni = list(reader)
    file.close()
except FileNotFoundError:
    print("Errore nell'apertura del file")
