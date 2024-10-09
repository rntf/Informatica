stringa = "questa è una stringa"
print(id(stringa))

print(stringa.upper())

# aggiorno il valore
stringa = "contenuto aggiornato"
print(id(stringa))

# anche int e float sono immutabili
valore = 10
print(id(valore))

valore = 15
print(id(valore))

print(stringa[5])
#stringa[5] = "t" # non si può fare