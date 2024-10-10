nome = input("Come ti chiami? ")
anno_nascita = int(input("In quale anno sei nato? "))

# Istruzioni equivalenti
#print("Il tuo nome è", nome)
#print("Il tuo nome è " + nome)
print(f"Il tuo nome è {nome}")

eta = 2024 - anno_nascita
#print("Hai", eta, "anni")
print(f"Hai {eta:<+20d} anni")

a = 10
print(f"Un terzo di 10 è {a / 3:.3f}")