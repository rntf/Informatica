# Scompongo in sottoproblemi
# 1)	Stampo la prima riga (intestazione)
# 2)	Stampo tutte le altre righe

# Sottoproblema 1
# Per ogni colonna
#   Stampo l’intestazione della colonna x^i

NUM_COLONNE = 4
for i in range(NUM_COLONNE):
    print(f"x^{i + 1:<10d}", end="")

print()

# Sottoproblema 2
