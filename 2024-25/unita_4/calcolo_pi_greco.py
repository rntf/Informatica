# Probabilità di colpire il cerchio = Area_cerchio / area quadrato
# r è il raggio del cerchio
# lato del quadrato è 2r

# pi r^2 / 4 r^2  = pi / 4

from random import uniform


contatore = 0

for i in range(100000):
    x = uniform(-1, 1)
    y = uniform(-1, 1)
    if x**2 + y ** 2 <= 1:
        contatore += 1

print(f"Il valore approssimato di pi greco è {contatore * 4 / 100000}")