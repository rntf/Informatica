##
# Il programma stampa tutte le parole contenute nel file,
# una per riga.
#

input_file = open("lyrics.txt", "r")

for line in input_file :
    word_list = line.split()
    for word in word_list :
        word = word.rstrip(".,?!")
        print(word)

input_file.close()
