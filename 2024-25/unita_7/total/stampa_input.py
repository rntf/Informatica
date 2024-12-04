# 1) apro i file
input_file = open("input.txt", "r")     # in lettura
output_file = open("output.txt", "w")   # in scrittura
totale = 0.0
num_valori = 0

# elaboro i file
#riga = input_file.readline()
#while riga != "":
for riga in input_file:
    # processo la riga corrente
    valore = float(riga)
    totale = totale + valore
    num_valori += 1
    output_file.write(f"{valore:14.2f}\n")
    # leggo la nuova riga del file
    #riga = input_file.readline()

media = totale / num_valori
output_file.write(f"Totale: {totale:.2f}\n")
output_file.write(f"Media: {media:.2f}\n")

# chiudo i file
input_file.close()
output_file.close()