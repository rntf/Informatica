def leggi_lista():
    lista = []
    user_input = input("Inserisci un numero ")
    while user_input.upper() != "Q":
        lista.append(int(user_input))
        user_input = input("Inserisci un numero ")
    return lista

def ordina_lista(lista):
    continua = True
    while continua:
        continua = False
        for i in range(len(lista) - 1):
            if lista[i] > lista[i + 1]:
                # scambio i due elementi
                # metodo 1: uso una variabile di appoggio
                # temp = lista[i]
                # lista[i] = lista[i + 1]
                # lista[i + 1] = temp

                # metodo 2: uso una tupla
                (lista[i], lista[i + 1]) = (lista[i + 1], lista[i])
                
                continua = True

    

def main():
    lista_da_ordinare = leggi_lista()
    # metodo 1: implementazione del bubble sort
    ordina_lista(lista_da_ordinare)
    # metodo 2: sort
    #lista_da_ordinare.sort()
    # metodo 3: funzione
    #lista_ordinata = sorted(lista_da_ordinare)
    print(f"La lista ordinata è {lista_da_ordinare}")

main()