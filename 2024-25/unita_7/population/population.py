##
#  Questo programma legge i dati di popolazione e superficie di nazioni
#  e scrive in un file la relativa densità, nazione per nazione.
#

POPULATION_FILE = "worldpop.txt"
AREA_FILE = "worldarea.txt"
REPORT_FILE = "world_pop_density.txt"


def main():
    # Apre i file.
    pop_file = open(POPULATION_FILE, "r")
    area_file = open(AREA_FILE, "r")
    report_file = open(REPORT_FILE, "w")

    # Legge il primo record di popolazione.
    pop_data = extract_data_record(pop_file)
    while len(pop_data) == 2:
        # Legge il successivo record di superficie.
        area_data = extract_data_record(area_file)

        # Estrae dalle due liste i campi dei record.
        country = pop_data[0]
        population = pop_data[1]
        area = area_data[1]

        # Calcola e scrive nel file la densità della nazione in esame.
        density = 0.0
        if area > 0:  # Evita divisioni per zero.
            density = population / area
        report_file.write(f"{country:40s} {density:15.2f}\n")

        # Legge il successivo record di popolazione.
        pop_data = extract_data_record(pop_file)

    # Chiude i file.
    pop_file.close()
    area_file.close()
    report_file.close()


def extract_data_record(infile):
    """
    Estrae e restituisce un record da un file di dati organizzato per 
    righe. Ogni riga contiene il nome di una nazione (eventualmente
    costituito da più parole) seguito da un numero intero (popolazione 
    oppure superficie della nazione).


    :param infile: il file da leggere
    :return: la lista contenente come primo elemento la nazione (stringa) 
    e come secondo elemento la popolazione o la superficie (un numero
    intero); raggiunta la fine del file, è restituita una lista vuota

    """
    line = infile.readline()
    if line == "":
        return []
    else:
        parts = line.rsplit(" ", 1)
        parts[1] = int(parts[1])
        return parts


# Inizio del programma.
main()
