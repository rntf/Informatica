##
#  Il programma calcola il numero di parole diverse presenti in un testo.
#

def main():
    filename = input("Enter filename (default: nurseryrhyme.txt): ")
    if len(filename) == 0:
        filename = "nurseryrhyme.txt"
    try:
        unique_words = read_words(filename)
        print("The document contains", len(unique_words), "unique words.")
    except FileNotFoundError:
        print(f"Errore nell'apertura del file {filename}")

def read_words(filename):
    """
    Dato un file, restituisce un **insieme** che contiene le parole uniche presenti nel file
    Attenzione: rimuove tutti i caratteri non alfabetici

    :param input_file: il nome del file da leggere
    :return: insieme contenente tutte le parole singole
    """
    input_file = open(filename, "r")
    unique_words = set()
    for line in input_file:
        the_words = line.split()
        for word in the_words:
            cleaned = clean(word)
            if cleaned != "":
                unique_words.add(cleaned)
    input_file.close()
    return unique_words
    

def clean(string):
    """
    Ripulisce una stringa rendendola minuscola e rimuovendo
    tutti i caratteri che non sono lettere.

    :param string: la stringa da ripulire
    :return: la stringa ripulita
    """
    result = ""
    for char in string:
        if char.isalpha():
            result = result + char.lower()

    return result


# Inizio del programma.
main()
