##
#   Questo programma legge una sequenza di lanci di un dado e
#   visualizza la frequenza di ciascun valore.
#

def main():
    counters = count_inputs(6)
    print_counters(counters)


def count_inputs(sides):
    """
    Legge una sequenza di lanci di un dado, con valori compresi tra 1 e 6
    (estremi inclusi) e conta la frequenza di ciascuna faccia.

    :param sides: il numero di facce del dado
    :return: una lista il cui i-esimo elemento contiene le occorrenze
    della faccia di valore i nei dati; l’elemento 0 è inutilizzato
    """
    counters = [0] * (sides + 1)  # counters[0] è inutilizzato.

    print("Please enter values, Q to quit:")
    user_input = input("")
    while user_input.upper() != "Q":
        value = int(user_input)

        # Incrementa il contatore corrispondente al valore acquisito.
        if 1 <= value <= sides:
            counters[value] = counters[value] + 1
        else:
            print(value, "is not a valid input.")

        # Acquisisce il valore successivo.
        user_input = input("")

    return counters


def print_counters(counters):
    """
    Visualizza una tabella con i valori dei contatori.

    :param counters: una lista di contatori; counters[0] non è visualizzato
    :return:
    """
    for i in range(1, len(counters)):
        print(f"{i}: {counters[i]}" )


# Inizio del programma.
main()
