occorrenze = [0] * 26
#stringa_lettere = "abcdefghijklmnopqrstuvwxyz"
# Leggo un carattere alla volta
input_file = open("lyrics.txt", "r")

carattere = input_file.read(1)
while carattere != "":
    # incremento il contatore corrispondente
    carattere = carattere.lower()
    if carattere.isalpha():
        posizione = ord(carattere) - ord("a")
    #if carattere in stringa_lettere:
    #    posizione = stringa_lettere.index(carattere)
        occorrenze[posizione] += 1

    # leggo il carattere successivo per la nuova iterazione
    carattere = input_file.read(1)

# stampo il risultato
# 'a': 7
# 'b': 2
# ...
for indice, elemento in enumerate(occorrenze):
    print(f"{chr(indice + ord('a'))}: {elemento}")

input_file.close()