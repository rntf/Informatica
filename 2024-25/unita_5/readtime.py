## 
#  Questo programma mostra il riutilizzo di una funzione.
#  

def main():
    print("Please enter a time: hours, then minutes.")
    hours = read_int_between(0, 23)
    minutes = read_int_between(0, 59)
    print(f"You entered {hours} hours and {minutes} minutes.")


def read_int_between(low, high):
    """
    Chiede all’utente di inserire un valore compreso in un certo intervallo,
    ripetutamente finché non viene introdotto un valore valido

    :param low: un numero intero, il valore minimo accettabile
    :param high: un numero intero, il valore massimo accettabile
    :return: il numero fornito dall’utente (tra low e high, compresi)
    """
    value = int(input("Enter a value between " + str(low) + " and " +
                      str(high) + ": "))
    while value < low or value > high:
        print("Error: value out of range.")
        value = int(input("Enter a value between " + str(low) + " and " +
                          str(high) + ": "))

    return value


# Inizio del programma.
main()
