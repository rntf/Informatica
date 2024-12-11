def main():
# apro i file
    input_popolazione = open("worldpop2.txt", "r")
    input_area = open("worldarea.txt", "r")
    output_densita = open("density.txt", "w")

    # memorizzare il secondo file in una struttura dati: uso una lista di liste
    # ripeto per tutte le righe del primo file
    #   leggo una riga dal primo file
    #   cerco nella struttura dati il record corrispondente
    #   calcolo la densità per la riga letta
    #   stampo la densità nel file di output
    tabella_popolazione = memorizza_file(input_popolazione)
    lista_area = estrai_valori(input_area)
    while len(lista_area) > 0:
        trovato = False
        i = 0
        while not trovato:
            if lista_area[0] == tabella_popolazione[i][0]:
                trovato = True
            else:
                i = i + 1

        if lista_area[1] > 0:
            densita = tabella_popolazione[i][1] / lista_area[1]
        else:
            densita = 0.0

        output_densita.write(f"{lista_area[0]} {densita:.2f}\n")
        lista_area = estrai_valori(input_area)



    # chiudo i file
    input_popolazione.close()
    input_area.close()
    output_densita.close()


def memorizza_file(input_file):
    tabella = []
    for riga in input_file:
        campi = riga.rsplit(maxsplit=1)
        tabella.append([campi[0], int(campi[1])])
    return tabella


def main_ordinato():
    # apro i file
    input_popolazione = open("worldpop.txt", "r")
    input_area = open("worldarea.txt", "r")
    output_densita = open("density.txt", "w")

    # ripeto per tutte le righe del primo file
    #   leggo una riga dal primo file e una riga dal secondo file
    #   calcolo la densità per la riga letta
    #   stampo la densità nel file di output
    lista_popolazione = estrai_valori(input_popolazione)
    lista_area = estrai_valori(input_area)
    while len(lista_popolazione) > 0:
        if lista_area[1] > 0:
            densita = lista_popolazione[1] / lista_area[1]
        else:
            densita = 0.0
        output_densita.write(f"{lista_popolazione[0]} {densita:.2f}\n")
        lista_popolazione = estrai_valori(input_popolazione)
        lista_area = estrai_valori(input_area)

    # chiudo i file
    input_popolazione.close()
    input_area.close()
    output_densita.close()

def estrai_valori(input_file):
    riga = input_file.readline()
    if riga != "":
        campi = riga.rsplit(maxsplit=1)
        return campi[0], int(campi[1])
    else:
        return []
    
main()