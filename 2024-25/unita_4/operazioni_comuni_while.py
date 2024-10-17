totale = 0
count = 0
count_valori_maggiori_50 = 0
count_consecutivi_uguali = 0

valore = int(input("Introduci un numero, valore negativo per terminare: "))
massimo = valore
minimo = valore

while valore >= 0:
    totale += valore
    if valore > massimo:
        massimo = valore
    elif valore < minimo:
        minimo = valore

    # conteggio valori in base ad una corrispondenza
    if valore > 50:
        count_valori_maggiori_50 += 1

    count += 1
    valore_precedente = valore
    valore = int(input("Introduci un numero, valore negativo per terminare: "))
    if valore == valore_precedente:
        count_consecutivi_uguali += 1
    
media = totale / count
print(f"Il totale è {totale}")
print(f"La media è {media}")
print(f"Il massimo è {massimo} e il minimo è {minimo}")
print(f"Hai inserito {count_consecutivi_uguali } valore consecutivi uguali")