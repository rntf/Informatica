stringa = "fine lezione"
# conto quante vocali ci sono nella stringa


indice = 0
contatore_vocali = 0
while indice < len(stringa):
    #if stringa[indice] == "a" or stringa[indice] == "e" or stringa[indice] == "i" or stringa[indice] == "o" or stringa[indice] == "u":
    if stringa[indice] in "aeiou":
        contatore_vocali += 1
    indice += 1

# equivalente
contatore_vocali = 0
for carattere in stringa:
    if carattere in "aeiou":
        contatore_vocali += 1

print(f"La stringa contiene {contatore_vocali} vocali")