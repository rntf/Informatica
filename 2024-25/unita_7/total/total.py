##
#  Il programma legge un file di numeri e li scrive in un altro file
#  incolonnati a destra e seguiti dal totale e dal valore medio.
#

# Chiede all'utente i nomi dei file, di input e di output.
input_file_name = input("Input file name: ")
output_file_name = input("Output file name: ")

# Apre i file di input e di output.
infile = open(input_file_name, "r")
outfile = open(output_file_name, "w")

# Legge i dati e scrive il file di output.
total = 0.0
count = 0

line = infile.readline()
while line != "":
    value = float(line)
    outfile.write(f"{value:15.2f}")
    total = total + value
    count = count + 1
    line = infile.readline()

# Scrive il totale e il valore medio.
outfile.write(f"{'--------':>15s}\n")
outfile.write(f"Total: {total:8.2f}\n")

avg = total / count
outfile.write(f"Average: {avg:6.2f}\n")

# Chiude i file.
infile.close()
outfile.close()
