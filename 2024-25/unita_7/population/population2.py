##
#  Legge i dati di popolazione e superficie da due file; l'ordine delle
#  nazioni nei due file è diverso. Scrive in un terzo file le densità. 
#

POPULATION_FILE = "worldpop2.txt"
AREA_FILE = "worldarea.txt"
REPORT_FILE = "world_pop_density2.txt"


def main():
    # Apre i file.
    area_file = open(AREA_FILE, "r")
    report_file = open(REPORT_FILE, "w")
    popolazione = save_file(POPULATION_FILE)

    # Legge il primo record di area.
    area_data = extract_data_record(area_file)
    while len(area_data) == 2:
        density = 0
        if area_data[1] > 0:
            # Cerca la nazione nella lista popolazione
            indice = 0
            trovato = False
            while indice < len(popolazione) and not trovato:
                if area_data[0].rstrip() == popolazione[indice][0]:
                    density = popolazione[indice][1] / area_data[1]
                    trovato = True
                indice += 1
        
        report_file.write(f"{area_data[0]:40s} {density:15.2f}\n")
        # Legge il successivo record di area.
        area_data = extract_data_record(area_file)
      
    # Chiude i file.
    area_file.close()
    report_file.close()


def save_file(file_name):
    """
    Estrae tutti i record da un file di dati organizzato per righe e li
    memorizza in una tabella. Ogni riga contiene il nome di una nazione
    (eventualmente costituito da più parole) seguito da un intero
    :param infile: il nome del file da leggere
    :return: la tabella con nazioni e popolazione corrispondente 
    """
    infile = open(file_name, "r")
    lines = []
    for line in infile:
        parts = line.rsplit(" ", 1)
        parts[0] = parts[0].rstrip()
        parts[1] = int(parts[1])
        lines.append(parts)
    infile.close()
    return lines


def extract_data_record(infile):
    """
    Estrae e restituisce un record da un file di dati organizzato per
    righe. Ogni riga contiene il nome di una nazione (eventualmente
    costituito da più parole) seguito da un numero intero (superficie).
    :param infile: il file da leggere
    :return: la lista contenente come primo elemento la nazione
    (stringa) e come secondo elemento la superficie (un numero intero);
    raggiunta la fine del file, è restituita una lista vuota
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

