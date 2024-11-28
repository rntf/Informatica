##
# Il programma legge un file le cui righe contengono articoli e prezzi.
#  nome articolo 1:prezzo 1
#  nome articolo 2:prezzo 2
#  ...
#  Ogni nome di articolo è terminato da un carattere "due punti".
#  Scrive un file in cui gli articoli sono incolonnati a sinistra e
#  i prezzi a destra. L'ultima riga contiene l’importo totale.
#

# Chiede i nomi dei file da leggere e da scrivere.
input_file_name = input("Input file: ")
output_file_name = input("Output file: ")

# Apre i file da leggere e da scrivere.
input_file = open(input_file_name, "r")
output_file = open(output_file_name, "w")

# Legge e scrive i file.
total = 0.0

for line in input_file:
    # Solo se nella riga c’è un carattere "due punti", la elabora.
    if ":" in line:
        # Suddivide il record in corrispondenza del "due punti"
        parts = line.split(":")

        # Estrae i due campi.
        item = parts[0]
        price = float(parts[1])

        # Aggiunge al totale.
        total = total + price

        # Scrive nel file.
        output_file.write(f'{item:<20s}{price:10.2f}\n')

# Scrive l’importo totale.
output_file.write(f'{"Total:":<20s}{total:10.2f}')

# Chiude i file.
input_file.close()
output_file.close()
