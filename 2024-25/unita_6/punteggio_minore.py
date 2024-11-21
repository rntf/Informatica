def rimuovi_minimo_due_cicli(lista):
    minimo = lista[0]
    for i in range(1, len(lista)):
        if lista[i] < minimo:
            minimo = lista[i]

    continua = True
    i = 0
    while i < len(lista) and continua:
        if lista[i] == minimo:
            lista.pop(i)
            continua = False

def rimuovi_minimo(lista):
    minimo = lista[0]
    posizione_minimo = 0
    for i in range(1, len(lista)):
        if lista[i] < minimo:
            minimo = lista[i]
            posizione_minimo = i

    lista.pop(posizione_minimo)

def rimuovi_due_minimi(lista):
    minimo1 = lista[0]
    posizione_minimo1 = 0
    minimo2 = lista[1]
    posizione_minimo2 = 1
    if minimo2 < minimo1:
        (minimo1, minimo2) = (minimo2, minimo1)
        (posizione_minimo1, posizione_minimo2) = (posizione_minimo2, posizione_minimo1)

    for i in range(2, len(lista)):
        if lista[i] < minimo1:
            minimo2 = minimo1
            posizione_minimo2 = posizione_minimo1

            minimo1 = lista[i]
            posizione_minimo1 = i
        elif lista[i] < minimo2:
                minimo2 = lista[i]
                posizione_minimo2 = i

    if posizione_minimo1 < posizione_minimo2:
        posizione_minimo2 = posizione_minimo2 - 1
    lista.pop(posizione_minimo1)
    lista.pop(posizione_minimo2)
    


#punteggi = [8, 7, 8.5, 9.5, 7, 4, 10]
punteggi = [8, 3, 7, 8.5, 9.5, 7, 4, 10]
# voglio rimuovere i 2 punteggi più bassi
# soluzione 1: funzioni predefinite, 2*N iterazioni
# minimo = min(punteggi)
# punteggi.remove(minimo)

# soluzione 2: algoritmi equivalenti, 2*N iterazioni
#rimuovi_minimo_due_cicli(punteggi)

# soluzione 3 migliore: un unico ciclo
#rimuovi_minimo(punteggi)
#rimuovi_minimo(punteggi)

# soluzione 4
rimuovi_due_minimi(punteggi)

print(punteggi)