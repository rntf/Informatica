from tabulardata import read_data, print_report


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


main()
