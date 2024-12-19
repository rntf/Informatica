# struttura dati: dizionario di insiemi
# - chiave del dizionario: keyword
# - valore associato alla chiave: inseme delle pagine in cui compare la keyword


# apro il file
# per ogni riga del file
#   estraggo pagina e keyword
#   se la keyword è già una chiave del dizionario:
#       aggiungo la pagina all'insieme di pagine associato alla chiave
#   altrimenti
#       aggiungo al dizionario la coppia keyword-pagina
# chiudo il file
# stampo la struttura dati

def main():
    dizionario = {}
    try:
        input_file = open("indexdata.txt", "r")
        for riga in input_file:
            (pagina, keyword) = riga.split(":")
            keyword = keyword.strip()
            pagina = int(pagina)
            if keyword in dizionario:
                insieme = dizionario[keyword]
                insieme.add(pagina)
            else:
                dizionario[keyword] = {pagina}

        input_file.close()
        stampo_indice_analitico(dizionario)
    except OSError:
        print("Il file non esiste")

def stampo_indice_analitico(dizionario):
    for chiave in sorted(dizionario.keys()):
        print(chiave, ": ", end="")
        for pagina in sorted(dizionario[chiave]):
            print(pagina, end=", ")
        print()

main()