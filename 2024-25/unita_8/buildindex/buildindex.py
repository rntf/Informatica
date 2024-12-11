## 
#  Questo programma costruisce l’indice analitico di un libro a partire
#  dai suoi termini e dai numeri di pagina in cui compaiono.
#

def main():
    # Crea un dizionario vuoto.
    index_entries = {}

    # Estrae i dati dal file di testo.
    try:
        infile = open("indexdata.txt", "r")
        fields = extract_record(infile)
        while len(fields) > 0:
            add_word(index_entries, fields[1], fields[0])
            fields = extract_record(infile)

        infile.close()
    except FileNotFoundError:
        print("Errore nell'apertura del file")

    # Visualizza l’indice analitico.
    print_index(index_entries)


def extract_record(infile):
    """
    Estrae dal file di testo un singolo record.

    :param infile: l’oggetto che rappresenta il file da leggere
    :return: una lista contenente un numero di pagina e un termine oppure una lista vuota se è stata raggiunta la fine del file
    """
    line = infile.readline()
    if line != "":
        fields = line.split(":")
        page = int(fields[0])
        term = fields[1].rstrip()
        return [page, term]
    else:
        return []


def add_word(entries, term, page):
    """
    Aggiunge all’indice una parola e il suo numero di pagina.

    :param entries: il dizionario di coppie parola/insiemeDiPagine
    :param term: il termine da aggiungere all’indice
    :param page: il numero di pagina di questa occorrenza del termine
    """
    # Se il termine è già nel dizionario, aggiunge la pagina al suo insieme.
    if term in entries:
        page_set = entries[term]
        page_set.add(page)

    # Altrimenti, crea un nuovo insieme con la pagina e inserisce una coppia.
    else:
        page_set = {page}
        entries[term] = page_set


def print_index(entries):
    """
    Visualizza l’indice analitico

    :param entries: il dizionario di coppie parola/insiemeDiPagine
    """
    for key in sorted(entries):
        print(key, end=" ")
        page_set = entries[key]
        first = True
        for page in sorted(page_set):
            if first:
                print(page, end="")
                first = False
            else:
                print(",", page, end="")

        print()


# Inizio del programma.
main()
