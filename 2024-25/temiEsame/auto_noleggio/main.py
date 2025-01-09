# - leggere il file in input con le auto disponibili
# - chiedere all’utente categoria di auto e i giorni in cui intende affittare
# - restituisce tutte le auto, se esistono, che soddisfano la richiesta 
# - oppure stampare il messaggio "Auto non disponibile" se non esistono auto che soddisfano le specifiche dell'utente.
# - scegliere un veicolo (Se esistono auto disponibili)
# - stampare a video l'elenco aggiornato di tutte le prenotazioni

def main():
    automobili = leggi_file("auto.csv")


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

main()