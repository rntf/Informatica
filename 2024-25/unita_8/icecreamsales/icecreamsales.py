## 
#  Questo programma elabora una raccolta di dati di vendita di vari
#  gusti di gelato e visualizza un rapporto ordinato per gusto.
#

def main():
    try:
        sales_data = read_data("icecream.txt")
        print_report(sales_data)
    except FileNotFoundError:
        print("Errore nell'apertura del file")

def read_data(filename):
    """
    Legge i dati della tabella.

    :param filename: nome del file da leggere
    :return: un dizionario: chiavi = gusti, valori = dati di vendita
    """
    # Crea un dizionario vuoto
    sales_data = {}

    infile = open(filename, "r")

    # Legge tutti i record presenti nel file. 
    for line in infile:
        fields = line.split(":")
        flavor = fields[0]
        sales_data[flavor] = build_list(fields)

    infile.close() 
    return sales_data


def build_list(fields):
    """
    Costruisce una lista con i dati di vendita presenti nei campi.

    :param fields: una lista di stringhe che contiene i campi di un record
    :return: una lista di valori in virgola mobile
    """
    store_sales = []
    for i in range(1, len(fields)):
        sales = float(fields[i])
        store_sales.append(sales)

    return store_sales


def print_report(sales_data):
    """
    Visualizza il rapporto delle vendite.
    :param sales_data: una tabella sotto forma di dizionario di liste
    """
    # Calcola il numero di negozi come lunghezza della lista più lunga.
    num_stores = 0
    for store_sales in sales_data.values():
        if len(store_sales) > num_stores:
            num_stores = len(store_sales)

    # Crea la lista dei totali di vendita per negozio.
    store_totals = [0.0] * num_stores

    # Visualizza le vendite per ciascun gusto di gelato.
    for flavor in sorted(sales_data):
        print(f'{flavor:15}', end='')

        flavor_total = 0.0
        store_sales = sales_data[flavor]
        for i in range(len(store_sales)):
            sales = store_sales[i]
            flavor_total = flavor_total + sales
            store_totals[i] = store_totals[i] + sales
            print(f'{sales:10.2f}', end='')

        print(f'{flavor_total:15.2f}')

    # Visualizza i totali per singolo negozio.
    print(" " * 15, end="")
    for i in range(num_stores):
        print(f'{store_totals[i]:10.2f}', end='')
    print()


# Inizio del programma.
main()
