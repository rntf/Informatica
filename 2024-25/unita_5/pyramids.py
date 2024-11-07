## 
#  Questo programma definisce una funzione che calcola il volume
#  di una piramide e contiene un suo collaudo di unità.
#

def main():
    print("Volume:", pyramid_volume(9, 10))
    print("Expected: 300")
    print("Volume:", pyramid_volume(0, 10))
    print("Expected: 0")


def pyramid_volume(height, base_length):
    """
    Calcola il volume di una piramide a base quadrata.

    :param height: un numero float che indica l’altezza della piramide
    :param base_length: un numero float che indica la lunghezza della base
    :return: il volume della piramide come valore di tipo float
    """
    base_area = base_length * base_length
    return height * base_area / 3


# Inizio del programma.
main()
