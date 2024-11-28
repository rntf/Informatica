##
#  Questo programma legge dati da un file CSV che contiene informazioni su
#  film, ignora i dati non desiderati e produce un nuovo file csv.
#

from csv import reader, writer

# Apre i due file CSV.
infile = open("movies.csv")
csv_reader = reader(infile)

outfile = open("filtered.csv", "w")
csv_writer = writer(outfile)

# Scrive nel file le intestazioni delle colonne.
headers = ["Name","Year","Actors"]
csv_writer.writerow(headers)

# Durante la lettura, ignora la riga con le intestazioni.
next(csv_reader)

# Esamina le righe con i dati.
for row in csv_reader :
  year = int(row[1])
  if year >= 1990 and year <= 1999 :
    new_row = [row[0], row[1], row[4]]
    csv_writer.writerow(new_row)
    
infile.close()
outfile.close()

