# Questo programma Python
# - legge l'elenco dei giocatori qualificati
# - restituisce tre file di output:
#       1) rosso.txt e verde.txt contenenti i due gironi sorteggiati, 
#       in cui devono essere specificati sia i nomi dei giocatori
#       sia il loro numero di testa di serie (in ordine crescente)
#       2) calendario.txt contenente l’elenco di tutti gli incontri,
#        divisi per girone e per giornata

# Scomposizione del problema
# 1) leggo il file di input e ottengo l'elenco dei giocatori
# 2) sorteggiare la composizione dei due gironi
# 3) stilare il calendario

from random import choice
def main():
    giocatori = leggi_file("qualificati.txt")
    verde, rosso = sorteggio_gironi(giocatori)
    stampa_gruppo("verde", verde)
    stampa_gruppo("rosso", rosso)
    genera_calendario("verde", verde, "calendario.txt")
    genera_calendario("rosso", rosso, "calendario.txt")



def leggi_file(input_file):
    # memorizzo il file in una lista
    giocatori = [""] * 9    # equivalente a giocatori = ["", "", "", "", "", "", "", ""]
    try:
        infile = open(input_file, "r")
        for line in infile:
            (testa_serie, nome) = line.split(",")
            giocatori[int(testa_serie)] = nome.strip()
        infile.close()
    except OSError:
        print(f"Il file {input_file} non esiste")
    
    return giocatori


def sorteggio_gironi(giocatori):
    # memorizzo i giocatori in due dizionari
    verde = {1: giocatori[1]}
    rosso = {2: giocatori[2]}

    for estrazione in range(3, 8, 2):
        coppia = [estrazione, estrazione + 1]
        selezionato = choice(coppia)
        verde[selezionato] = giocatori[selezionato]
        coppia.remove(selezionato)
        rosso[coppia[0]] = giocatori[coppia[0]]

    return verde, rosso

def stampa_gruppo(nome_gruppo, gruppo):
    try:
        output_file = open(nome_gruppo + ".txt", "w")
        output_file.write(f"Girone {nome_gruppo}\n")
        for (testa_serie, giocatore) in gruppo.items():
            output_file.write(f"{testa_serie} - {giocatore}\n")
        
        output_file.close()
    except OSError:
        print(f"Impossibile scrivere il file {nome_gruppo}.txt")

def genera_calendario(nome_gruppo, gruppo, nome_file):
    # trovo il primo giocatore
    prima_testa_di_serie = min(gruppo.keys())
    primo_giocatore = gruppo[prima_testa_di_serie]
    # genero una lista con tutti gli altri
    avversari = list(gruppo.values())
    avversari.remove(primo_giocatore)
    copia_avversari = avversari.copy()

    try:
        output_file = open(nome_file, "a")
        output_file.write(f"Gruppo {nome_gruppo}\n")
        giornata = 1
        while len(avversari) > 0:
            output_file.write(f"Giornata: {giornata}\n")
            giornata += 1
            avversario_primo_giocatore = choice(avversari)
            output_file.write(f"{primo_giocatore} vs {avversario_primo_giocatore}\n")
            avversari.remove(avversario_primo_giocatore)

            copia_avversari.remove(avversario_primo_giocatore)
            output_file.write(f"{copia_avversari[0]} vs {copia_avversari[1]}\n")
            copia_avversari.append(avversario_primo_giocatore)

        output_file.close()
    except OSError:
        print(f"Impossibile scrivere il file {nome_file}.txt")



main()