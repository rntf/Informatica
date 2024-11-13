##
#  Questo programma legge, scala e inverte una sequenza di numeri.
#

def main():
    numbers = read_floats(5)
    multiply(numbers, 10)
    print_reversed(numbers)


def read_floats(number_of_inputs):
    """
    Legge una sequenza di numeri in virgola mobile

    :param number_of_inputs: il numero di valori da leggere
    :return: una lista contenente i valori letti
    """
    print("Enter", number_of_inputs, "numbers:")
    inputs = []
    for i in range(number_of_inputs):
        value = float(input(""))
        inputs.append(value)

    return inputs


def multiply(values, factor):
    """
    Moltiplica per uno stesso fattore gli elementi di una lista.

    :param values: una lista di numeri
    :param factor: il fattore per cui moltiplicare gli elementi
    """
    for i in range(len(values)):
        values[i] = values[i] * factor


def print_reversed(values):
    """
    Visualizza una lista in ordine inverso.

    :param values: una lista di numeri
    """
    # Ispeziona la lista in ordine inverso, partendo dall’ultimo elemento
    i = len(values) - 1
    while i >= 0:
        print(values[i], end=" ")
        i = i - 1
    print()


# Inizio del programma.
main()
