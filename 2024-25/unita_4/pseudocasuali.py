from random import randint, random, uniform

# genero un numero casuale compreso fra 1 e 10
for indice in range(20):
    pseudo_casuale = randint(1, 10)
    print(f"numero {indice + 1}: {pseudo_casuale}")

# genero un numero casuale fra 0.0 e 1.0
numero_reale = random()
print(numero_reale)

# genero un numero casuale fra 2.5 e 6.8
intervallo = 6.8 - 2.5
numero_reale1 = random()
# amplio l'intervallo: da 1 a (6.8 - 2.5).
# Ho un numero compreso fra 0 e 4.3
numero_reale2 = numero_reale1 * intervallo
# Ottengo un numero compreso tra 2.5 e 6.8
numero_reale3 = numero_reale2 + 2.5
print(numero_reale3)

# equivalente a
numero_reale4 = uniform(2.5, 6.8)
print(numero_reale4)