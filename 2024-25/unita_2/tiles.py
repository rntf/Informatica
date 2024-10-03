##
#  Calcola il numero di piastrelle necessarie e lo spazio a ciascuna 
#  estremità della riga, quando posiziona una fila di piastrelle lungo il muro
#

# Definisce le dimensioni.
total_width = 100
tile_width = 5

# Calcola il numero di piastrelle e lo spazio.
number_of_pairs = (total_width - tile_width) // (2 * tile_width)
number_of_tiles = 1 + 2 * number_of_pairs
gap = (total_width - number_of_tiles * tile_width) / 2.0

print("Number of tiles:", number_of_tiles)
print("Gap at each end:", gap)

