# Scompongo in sottoproblemi
# 1)	Stampo la prima riga (intestazione)
# 2)	Stampo tutte le altre righe


# assegnazione valore alle costanti
NUM_COLONNE = 6
NUM_RIGHE = 12

# Sottoproblema 1
# Per ogni colonna
#   Stampo l’intestazione della colonna x^i

for i in range(NUM_COLONNE):
    print(f"x^{i + 1:<10d}", end="")

print()

# Sottoproblema 2
#Per ogni riga
#   Per ogni colonna nella riga:
#       Stampo l’elemento i-esimo

for base in range(1, NUM_RIGHE + 1):
    for esponente in range(1, NUM_COLONNE + 1):
        print(f"{base**esponente:<12d}", end="")
    print()

a = 3
b = 5
print("Il risultato di", a, "più", b, "è", a+b, sep="--")
