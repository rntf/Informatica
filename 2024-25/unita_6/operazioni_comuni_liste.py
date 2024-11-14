lista_numeri = [2, 7, 1, 9, 10]
print(id(lista_numeri))
lista_numeri[1] = -5    # possibile perché la lista è mutabile

lista_numeri = [1, 2, 3, 4, 5]
print(id(lista_numeri))     # ouput diverso: la lista è ricreata



lista_caratteri = ['i', 'n', 'f', 'o', 'r']
lista_stringhe = ["informatica", "analisi matematica", "chimica"]
lista_numeri_reali = [3.14, 15.6, 56.2]
lista_mista = [1, 'i', "informatica", 3.14] # corretto ma non è una buona idea


# stampo l'intera lista
print(lista_numeri)
# stampo il terzo elemento della lista
print(lista_numeri[2])

# le liste sono simili alle stringhe ma con 2 differenze:
# 1) le liste contengono qualunque tipo di dato
# 2) le liste sono mutabili
parola = "informatica"
print(id(parola))
# stampo la terza lettera
print(parola[2])
parola = "chimica"  # distruggo la variabile e ne creo una nuova
print(id(parola))



lista_numeri = [2, 7, 9, 10, 7]
# voglio stampare la posizione dell'elemento e il valore corrispondente

# itero sugli indici della lista
for indice in range(len(lista_numeri)):
    print(indice, "-", lista_numeri[indice])
    
# itero sui valori della lista
indice = 0
for valore in lista_numeri:
    print(indice, "-", valore)
    indice += 1
    
for (indice, valore) in enumerate(lista_numeri):
    print(indice, "-", valore)



lista_numeri = [2, 7, 9, 10, 7]

print(lista_numeri[2])  # stampo 9
print(lista_numeri[-2]) # stampo 10

# stampo la lista in ordine inverso usando indici negativi
for indice in range(-1, -len(lista_numeri) -1, -1):
    print(lista_numeri[indice])
    
# stampo la lista in ordine inverso usando indici positivi
for indice in range(len(lista_numeri) -1, -1, -1):
    print(lista_numeri[indice])



lista_numeri = [2, 7, 9, 10, 7]

# copio il riferimento alla zona di memoria
lista2 = lista_numeri  
lista2[1] = 11
print(lista_numeri[1])  # stampo 11

# copiare il contenuto
lista3 = list(lista_numeri)
lista3[1] = 15
print(lista_numeri[1])  # stampo 11


lista_numeri = [2, 7, 9, 10, 7]

lista_numeri.append(13)     # aggiunge un elemento alla fine della lista
lista_numeri.insert(2, 19)  # aggiunge 19 in posizione 2



lista_numeri = [2, 7, 9, 10, 7, 3, 5, 7, 8]

# voglio sapere se l'elemento 7 è contenuto nella lista
valore_da_cercare = 7
if valore_da_cercare in lista_numeri:
    print(f"L'elemento {valore_da_cercare} è presente nella lista")
    # voglio sapere la posizione dell'elemento 7
    posizione1 = lista_numeri.index(valore_da_cercare)
    print(f"Si trova in posizione {posizione1}")
    
    # devo verificare se il valore da cercare è presente nel resto della lista
    if valore_da_cercare in lista_numeri[posizione1 + 1: ]:
        posizione2 = lista_numeri.index(valore_da_cercare, posizione1 + 1)
        print(f"Si trova anche in posizione {posizione2}")
    
else:
    print(f"L'elemento {valore_da_cercare} non è presente nella lista")



lista_numeri = [2, 7, 9, 10, 7, 3, 5, 7, 8]
valore_da_cercare = 7
# voglio stampare tutte le posizioni in cui compare il valore da cercare

# soluzione 1 con index: eseguo un ciclo tante volte quante sono le occorrenze del valore da cercare
posizione = -1

while valore_da_cercare in lista_numeri[posizione + 1: ]:
    posizione = lista_numeri.index(valore_da_cercare, posizione + 1)
    print(f"L'elemento {valore_da_cercare} si trova in posizione {posizione}")
    
# soluzione 2: itero su tutti gli elementi
for (indice, valore) in enumerate(lista_numeri):
    if valore == valore_da_cercare:
        print(f"L'elemento {valore_da_cercare} si trova in posizione {indice}")




lista_numeri = [2, 7, 9, 10, 7, 3, 5, 7, 8]

# tolgo l'ultimo elemento
valore_tolto1 = lista_numeri.pop()

# tolgo il terzo elemento
valore_tolto2 = lista_numeri.pop(2)

# tolgo l'elemento con valore 3
valore_restituito = lista_numeri.remove(3)




lista_numeri = [2, 7, 9, 10, 7, 3, 5, 7, 8]
lista_caratteri = ['a', 'b', 'c', 'd']

# concateno le due lista
lista3 = lista_numeri + lista_caratteri

# soluzione analoga con il metodo extend
lista4 = []
lista4.extend(lista_numeri)
lista4.extend(lista_caratteri)

#lista4 = lista4.extend(lista_numeri) # errore: lista4 è None

lista5 = []
lista5.append(lista_numeri)
lista5.append(lista_caratteri)


lista_numeri = [2, 7, 9, 10, 7, 3, 5, 7, 8]
minimo = min(lista_numeri)
massimo = max(lista_numeri)
somma = sum(lista_numeri)

lista_decrescente = sorted(lista_numeri, reverse=True)
lista_numeri.sort(reverse=True)
