##
#  Questo programma simula il lancio di un paio di dadi.
#

from random import randint

for i in range(10):
    # Genera due numeri interi casuali compresi
    # tra 1 e 6, estremi inclusi
    d1 = randint(1, 6)
    d2 = randint(1, 6)

    # Visualizza i due valori.
    print(d1, d2)
