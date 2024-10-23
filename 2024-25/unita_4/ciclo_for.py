stringa = "abcde"

indice = 0
while indice < len(stringa):
    print(f"il carattere in posizione {indice} è {stringa[indice]}")
    indice += 1

# ciclo for equivalente - "lungo"
indice = 0
for lettera in stringa:
    print(f"il carattere in posizione {indice} è {lettera}")
    indice += 1

# ciclo for equivalente - "compatto"
for (indice, lettera) in enumerate(stringa):
    print(f"il carattere in posizione {indice} è {lettera}")