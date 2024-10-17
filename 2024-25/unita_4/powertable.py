##
#  Questo programma visualizza una tabella con le potenze di x.
#

# Inizializza le costanti per i valori massimi.
NMAX = 4
XMAX = 10

# Visualizza l’intestazione della tabella.
for n in range(1, NMAX + 1):
    nome_colonna = "x^" + str(n)
    print(f"{nome_colonna:>10s}", end="")

print("\n", "    ", "-" * (5 + 10 * (NMAX - 1)))

# Visualizza il corpo della tabella.
for x in range(1, XMAX + 1):
    # Visualizza la riga x della tabella.
    for n in range(1, NMAX + 1):
        print(f"{x ** n:10d}", end="")

    print()
