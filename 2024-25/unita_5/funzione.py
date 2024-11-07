from random import random

def volumeCubo(lato):
    """
    Calcola il volume di un cubo
    
    :param lato: il lato del cubo
    :return: il volume del cubo
    """
    volume = lato ** 3
    return volume


def volumeParallelepipedo(lato1, lato2, lato3=1):
    """
    Calcola il volume di un parallelepipedo.
    Se non specifico la profondità, si intende profondità 1
    
    :param lato1: base
    :param lato2: altezza
    :param lato3: profondità
    :return: il volume del parallelepipedo
    """
    volume = lato1 * lato2 * lato3
    return volume

# chiamo la funzione con parametri posizionali
risultato1 = volumeParallelepipedo(5, 8, 10)
print(risultato1)

# chiamo la funzione con parametri nominali
risultato2 = volumeParallelepipedo(lato3 = 15, lato1 = 2, lato2 = 7)
print(risultato2)

# chiamo la funzione con un parametro posizionale e 2 parametri nominali
risultato2 = volumeParallelepipedo(15, lato3 = 8, lato2 = 7)
print(risultato2)

# chiamo la funzione con 2 parametri posizionali
risultato3 = volumeParallelepipedo(15, 9)   # sottintendo lato3 = 1
print(risultato3)


# chiamo la funzione passando un valore immediato
risultato1 = volumeCubo(20)
print(f"Il volume di un cubo di lato 20 è {risultato1}")

# chiamo la funzione passando una variabile
lato = 30
risultato2 = volumeCubo(lato)
print(f"Il volume di un cubo di lato {lato} è {risultato2}")

# uso un valore calcolato a run time come parametro
risultato3 = volumeCubo(random())
print(f"Il volume di un cubo di lato casuale è {risultato3}")


