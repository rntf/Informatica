# - leggere il file in input con le auto disponibili
# - chiedere all’utente categoria di auto e i giorni in cui intende affittare
# - restituisce tutte le auto, se esistono, che soddisfano la richiesta 
# - oppure stampare il messaggio "Auto non disponibile" se non esistono auto che soddisfano le specifiche dell'utente.
# - scegliere un veicolo (Se esistono auto disponibili)
# - stampare a video l'elenco aggiornato di tutte le prenotazioni

def main():
    lista_auto = leggi_file("auto.csv")
    (categoria, giorni) = chiedi_auto()
    lista_auto_prenotabili = trova_auto(categoria, giorni, lista_auto)
    if len(lista_auto_prenotabili) == 0:
        print("Auto non disponibile")
    else:
        scelta = scegli_auto(lista_auto, lista_auto_prenotabili)
        aggiorna_struttura_dati(lista_auto, scelta, giorni)


def leggi_file(nomefile):
    # memorizzo il file in una lista di dizionari
    lista = []
    try:
        input_file = open(nomefile, "r")
        input_file.readline()     #consumo la prima riga
        for riga in input_file:
            dizionario = {}
            campi = riga.strip().split(",")
            dizionario["categoria"] = campi[0]
            dizionario["marca"] = campi[1]
            dizionario["modello"] = campi[2]
            dizionario["colore"] = campi[3]
            dizionario["disponibilita"] = campi[4:]
            lista.append(dizionario)
        input_file.close()

    except OSError:
        print(f"Il file {nomefile} non esiste")

    return lista


def chiedi_auto():
    risposta = input("Scegli categoria e giorni: ")
    campi = risposta.split()
    return (campi[0], campi[1:])

def trova_auto(categoria, giorni, lista_auto):
    auto_prenotabili = []

    for (indice, auto) in enumerate(lista_auto):
        valido = True
        if auto["categoria"] == categoria:
            for giorno in giorni:
                if auto["disponibilita"][int(giorno) - 1] == "A":
                    valido = False
        
            if valido:
                auto_prenotabili.append(indice)
    
    return auto_prenotabili


def scegli_auto(lista_auto, lista_auto_prenotabili):
    print("Le macchine disponbili sono:")
    opzione = 1
    for indice in lista_auto_prenotabili:
        print(f'{opzione}) {lista_auto[indice]["marca"]} {lista_auto[indice]["modello"]} {lista_auto[indice]["colore"]}')
        opzione += 1

    scelta = input("Quale vuoi prenotare? ")
    return lista_auto_prenotabili[int(scelta) - 1]


def aggiorna_struttura_dati(lista_auto, scelta, giorni):
    for giorno in giorni:
        lista_auto[scelta]["disponibilita"][int(giorno) - 1] = "A"

    for auto in lista_auto:
        print(f"\n{auto['categoria']} {auto['marca']} {auto['modello']} {auto['colore']}", end="")
        for giorno in auto['disponibilita']:
            print(" ", giorno, end="")
        

main()