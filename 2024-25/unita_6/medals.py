##
#  Questo programma visualizza una tabella di medaglie,
#  con i totali per riga
#

MEDALS = 3
COUNTRIES = 8

# Crea una lista con i nomi delle nazioni.
countries = ["Canada",
             "Italy",
             "Germany",
             "Japan",
             "Kazakhstan",
             "Russia",
             "South Korea",
             "United States"]

# Crea una tabella con il numero di medaglie.              
counts = [
    [0, 3, 0],
    [0, 0, 1],
    [0, 0, 1],
    [1, 0, 0],
    [0, 0, 1],
    [3, 1, 1],
    [0, 1, 0],
    [1, 0, 1]
]

# Visualizza l'intestazione della tabella.
print("        Country    Gold  Silver  Bronze   Total")

# Visualizza nazioni, numero di singole medaglie e totali per riga.
for i in range(COUNTRIES):
    print(f"{countries[i]:15s}", end="")

    # Visualizza tutti gli elementi della riga.
    total = 0
    for j in range(MEDALS):
        print(f"{counts[i][j]:8d}", end="")
        total = total + counts[i][j]

    # Visualizza il totale della riga e va a capo.
    print(f"{total:8d}")
