##
#  Questo programma scambia tra loro le due metà di una lista.
#

def main():
    values = [9, 13, 21, 4, 18, 11, 7, 1, 3]

    # Se la lista ha lunghezza dispari, come diventa dopo lo scambio?
    # 1) [11, 7, 1, 3, 9, 13, 21, 4, 18]
    # 2) [18, 11, 7, 1, 3, 9, 13, 21, 4]
    # 3) [11, 7, 1, 3, 18, 9, 13, 21, 4]
    # 4) [18, 11, 7, 1, 9, 13, 21, 4, 3]
    #i = 0
    j = (len(values) + 1)  // 2
    values = values[j:] + values[:j]
    
    #while i < len(values) // 2:
    #    (values[i], values[j]) = (values[j], values[i])
    #    i = i + 1
    #    j = j + 1

    print(values)


def swap(a, i, j):
    """
    Scambia due elementi di una lista, date le loro posizioni.

    :param a: la lista
    :param i: la prima posizione
    :param j: la seconda posizione
    """
    #temp = a[i]
    #a[i] = a[j]
    #a[j] = temp
    (a[i], a[j]) = (a[j], a[i])

# Inizio del programma.
main()
