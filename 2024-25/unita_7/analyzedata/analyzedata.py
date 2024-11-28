##
#  Questo programma elabora un file con un conteggio, seguito da valori.
#  Se non esiste o non è corretto, l’utente può fornire un altro nome.
#

def main():
    done = False
    while not done:
        try:
            filename = input("Please enter the file name: ")
            data = read_file(filename)

            # Come esempio di elaborazione dei dati, ne calcoliamo la somma.
            total = 0
            for value in data:
                total = total + value

            print("The sum is", total)
            done = True

        except IOError:
            print("Error: file not found.")

        except ValueError:
            print("Error: file contents invalid.")

        except RuntimeError as error:
            print("Error:", str(error))


def read_file(filename):
    """
    Apre un file e legge un insieme di dati.

    :param filename: il nome del file che contiene i dati
    :return: una lista contenente i dati acquisiti dal file
    """
    infile = open(filename, "r")
    try:
        return read_data(infile)
    finally:
        infile.close()


def read_data(infile):
    """
    Legge un insieme di dati.

    :param infile: il file contenente i dati
    :return: una lista contenente i dati acquisiti dal file
    """
    line = infile.readline()
    number_of_values = int(line)  # Può sollevare un’eccezione ValueError.
    data = []

    for i in range(number_of_values):
        line = infile.readline()
        value = float(line)  # Può sollevare un’eccezione ValueError.
        data.append(value)

    # Controlla che non ci siano altri valori nel file.
    line = infile.readline()
    if line != "":
        raise RuntimeError("End of file expected.")

    return data


# Inizio del programma.
main()
