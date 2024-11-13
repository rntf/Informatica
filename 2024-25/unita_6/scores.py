##
#  Questo programma calcola il punteggio complessivo di una sequenza di
#  voti, sommandoli dopo aver eliminato i due più bassi. Usa una lista.

#

def main():
    scores = read_floats()
    if len(scores) > 1:
        remove_minimum(scores)
        remove_minimum(scores)
        total = sum(scores)
        print("Final score:", total)
    else:
        print("At least two scores are required.")


def read_floats():
    """
    Legge una sequenza di numeri in virgola mobile.

    :return: a list containing the numbers
    """

    # Crea una lista vuota.
    values = []

    # Legge i valori in ingresso e li scrive nella lista.
    print("Please enter values, Q to quit:")
    user_input = input("")
    while user_input.upper() != "Q":
        values.append(float(user_input))
        user_input = input("")

    return values


def remove_minimum(values):
    """
    Elimina il valore minimo da una lista

    :param values: una lista di dimensione >= 1
    """

    smallest_position = 0
    for i in range(1, len(values)):
        if values[i] < values[smallest_position]:
            smallest_position = i

    values.pop(smallest_position)


# Inizio del programma.
main()
