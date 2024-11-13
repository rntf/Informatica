##
#  Questo programma scambia tra loro le due metà di una lista.
#

def main():
    values = [9, 13, 21, 4, 11, 7, 1, 3]
    i = 0
    j = len(values) // 2
    while i < len(values) // 2:
        swap(values, i, j)
        i = i + 1
        j = j + 1
    
    # Il ciclo è equivalente a:
    # values = values[j:len(values)] + values[0:j]

    print(values)


def swap(a, i, j):
    """
    Scambia due elementi di una lista, date le loro posizioni.

    :param a: la lista
    :param i: la prima posizione
    :param j: la seconda posizione
    """
    temp = a[i]
    a[i] = a[j]
    a[j] = temp


# Inizio del programma.
main()
