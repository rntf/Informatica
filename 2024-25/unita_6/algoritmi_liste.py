def main():
    lista = []
    # riempire la lista con 7 elementi
    for i in range(7):
        lista.append(i ** 2)

    # Operazione 1: sommare gli elementi della lista
    # somma = sum(lista) # utilizzabile solo se la lista contiene numeri

    # metodo generale valido per ogni tipo di lista
    somma = 0
    for elemento in lista:
        somma = somma + elemento
    print(f"La somma degli elementi è {somma}")

    giorni = ["lunedì", "martedì", "mercoledì", "giovedì", "venerdì", "sabato"]
    concatenazione = ""
    for (indice, elemento) in enumerate(giorni):
        if indice == 0:
            concatenazione = elemento
        else:
            concatenazione = concatenazione + ", " + elemento
    #print(f"I giorni lavorativi della settimana sono: {concatenazione}")

    # alternativa
    concatenazione = giorni[0]
    for i in range(1, len(giorni)):
        concatenazione = concatenazione + ", " + giorni[i]
    #print(f"I giorni lavorativi della settimana sono: {concatenazione}")
   
    # alternativa 2
    concatenazione = ", ".join(giorni)
    print(f"I giorni della settimana sono: {concatenazione}")
   
    # Operazione 2: ricerca del minimo
    #minimo = min(lista)

    # alternativa tramite un ciclo
    minimo = lista[0]
    for indice in range(1, len(lista)):
        if lista[indice] < minimo:
            minimo = lista[indice]
    print(f"Il valore minimo è {minimo}")

    # problema simile: trovare il giorni della settimana con il nome più breve
    minimo = len(giorni[0])
    giorno_breve = giorni[0]
    for indice in range(1, len(giorni)):
        if len(giorni[indice]) < minimo:
            minimo = len(giorni[indice])
            giorno_breve = giorni[indice]
    print(f"Il giorno con il nome più breve è {giorno_breve}")

    # problema simile: trovare il giorno della settimana con il nome più lungo
    massimo = len(giorni[0])
    giorno_lungo = giorni[0]
    for indice in range(1, len(giorni)):
        if len(giorni[indice]) > massimo:
            massimo = len(giorni[indice])
            giorno_lungo = giorni[indice]
    print(f"Il giorno con il nome più lungo è {giorno_lungo}")

    # Operazione 3: ricerca di un'occorrenza
    # voglio trovare il valore 16
    valore_da_cercare = 16
    if valore_da_cercare in lista:
        posizione = lista.index(valore_da_cercare)
        print(f"Il valore {valore_da_cercare} si trova in posizione {posizione}")
    else:
        print(f"Il valore {valore_da_cercare} non si trova nella lista")
    
    # alternativa
    #for (indice, elemento) in enumerate(lista):
    indice = 0
    continua = True
    while indice < len(lista) and continua:
        if lista[indice] == valore_da_cercare:
            posizione = indice
            continua = False
        indice += 1

    if continua:
        print(f"Il valore {valore_da_cercare} non si trova nella lista")
    else:
        print(f"Il valore {valore_da_cercare} si trova in posizione {posizione}")
    
    # problema: trovare il primo elemento che sta all'interno di un intervallo
    # cercare il primo elemento compreso tra 20 e 40
    indice = 0
    continua = True
    while indice < len(lista) and continua:
        if 20 < lista[indice] < 40:
            posizione = indice
            continua = False
        indice += 1

    if continua:
        print(f"Nessun elemento della lista è compreso fra 20 e 40")
    else:
        print(f"Il primo elmento compreso fra 20 e 40 si trova in posizione {posizione}")
    
    # contare corrispondenze
    # Voglio contare tutti gli elementi compresi fra 20 e 40
    contatore = 0
    for indice in range(len(lista)):
        if 20 < lista[indice] < 40:
            contatore += 1
    print(f"Nella lista ci sono {contatore} elementi compresi fra 20 e 40")

    # Operazione: rimuovere una corrispondenza
    # Voglio rimuovere l'elemento con valore 16
    #lista.remove(16)
    
    # alternativa
    # equivalente al remove: toglie solo la prima occorrenza di 16
    indice = 0
    continua = True
    while indice < len(lista) and continua:
        if lista[indice] == 16:
            lista.pop(indice)
            continua = False
        indice += 1
    
    lista = [3, 4, 16, 15, 3, 16, 24]
    # problema simile: tolgo tutte le occorrenze del valore
    indice = 0
    while indice < len(lista):
        if lista[indice] == 16:
            lista.pop(indice)
        else:
            indice += 1

    print(lista)


main()