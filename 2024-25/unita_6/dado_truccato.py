# Soluzione formale per il problema generale
# 1) Acquisizione dell'input
# 2) Analisi dei dati acquisiti e calcolo del risultato
# 3) Stampa del risultato

# Soluzione formale dettagliata per il problema specifico
# 1) Chiedo all'utente i lanci del dado e memorizzo in una lista
# 2) Conto le occorrenze all'interno della lista
# 3) Stampo le occorrenze per ciascun valore del dato
# -> Spreca memoria per il punto 1

# -> Soluzione più efficiente
# 1) Per ogni dato inserito dall'utente, processalo (incrementa contatore)
# 2) Stampo il risultato (contatori)

from random import randint

def main():
    contatori = processa_input(100000, 6)
    # ad esempio se contatori = [3, 5, 3, 1, 2, 4] 
    # significa che "1" è uscito 3 volte, "2" è uscito 5 volte e così via
    stampa_risultato(contatori)

def processa_input(num_lanci, num_facce):
    lista = [0] * num_facce
    # equivalente a lista = [0, 0, 1, 0, 0, 0]

    # calcolo
    for i in range(num_lanci):
        valore_casuale = randint(1, num_facce)
        lista[valore_casuale - 1] += 1

    return lista

def stampa_risultato(lista):
    for i in range(len(lista)):
        print(f"Il valore {i + 1} è uscito {lista[i]} volte")

main()