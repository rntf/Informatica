# Leggo una parola alla volta
input_file = open("lyrics.txt", "r")
for riga in input_file:
    parole = riga.split()
    for parola in parole:
        print(parola.rstrip(".,;:\n"))


input_file.close()