def main():
    primo_numero_6_bit = input("Inserisci il primo numero binario su 6 bit:")
    secondo_numero_6_bit = input("Inserisci il secondo numero binario su 6 bit:")

    (risultato, overflow) = somma_binario_puro(primo_numero_6_bit, secondo_numero_6_bit)
    if overflow:
        stringa_overflow = "con"
    else:
        stringa_overflow = "senza"
    print(f"La somma in binario puro su 6 bit è {risultato} {stringa_overflow} overflow")

    (risultato, overflow) = somma_ca2(primo_numero_6_bit, secondo_numero_6_bit)
    if overflow:
        stringa_overflow = "con"
    else:
        stringa_overflow = "senza"
    print(f"La somma in complemento a 2 su 6 bit è {risultato} {stringa_overflow} overflow")

    (risultato, overflow) = sottrazione_ca2(primo_numero_6_bit, secondo_numero_6_bit)
    if overflow:
        stringa_overflow = "con"
    else:
        stringa_overflow = "senza"
    print(f"La sottrazione in complemento a 2 su 6 bit è {risultato} {stringa_overflow} overflow")

    numero_base_10 = int(input("Inserisci un numero in base 10: "))
    numero_binario = da_decimale_a_binario(numero_base_10)
    if len(numero_binario) <= 8:
        zero_iniziali = 8 - len(numero_binario)
        numero_binario = "0" * zero_iniziali + numero_binario
        print(f"Il numero {numero_base_10} in base 10 corrisponde al numero {numero_binario} in ca2 su 8 bit")
    else:
        print(f"Il numero {numero_base_10} in base 10 non è rappresentabile in ca2 su 8 bit ({numero_binario})")


def somma_binario_puro(primo_numero, secondo_numero):
    risultato = ""
    riporto = 0
    for indice in range(len(primo_numero) - 1, -1, -1):
        bit_primo = int(primo_numero[indice])
        bit_secondo = int(secondo_numero[indice])
        bit_risultato = bit_primo + bit_secondo + riporto
        if bit_risultato == 2:
            bit_risultato = 0
            riporto = 1
        else:
            riporto = 0
        risultato = str(bit_risultato) + risultato
    
    overflow = (riporto == 1)
    return (risultato, overflow)


def somma_ca2(primo_numero, secondo_numero):
    risultato = ""
    riporto = 0
    for indice in range(len(primo_numero) - 1, -1, -1):
        bit_primo = int(primo_numero[indice])
        bit_secondo = int(secondo_numero[indice])
        bit_risultato = bit_primo + bit_secondo + riporto
        if bit_risultato == 2:
            bit_risultato = 0
            riporto = 1
        else:
            riporto = 0
        risultato = str(bit_risultato) + risultato
    
    if primo_numero[0] == secondo_numero[0] and primo_numero[0] != risultato[0]:
        overflow = True
    else:
        overflow = False

    return (risultato, overflow)


def sottrazione_ca2(primo_numero, secondo_numero):
    risultato = ""
    prestito = 0
    for indice in range(len(primo_numero) - 1, -1, -1):
        bit_primo = int(primo_numero[indice])
        bit_secondo = int(secondo_numero[indice])
        bit_risultato = bit_primo - bit_secondo - prestito
        if bit_risultato < 0:
            bit_risultato += 2
            prestito = 1
        else:
            prestito = 0
        risultato = str(bit_risultato) + risultato
    
    if primo_numero[0] != secondo_numero[0] and primo_numero[0] != risultato[0]:
        overflow = True
    else:
        overflow = False

    return (risultato, overflow)


def da_decimale_a_binario(numero_base_10):
    risultato = ""
    while numero_base_10 > 0:
        resto = numero_base_10 % 2
        risultato = str(resto) + risultato
        numero_base_10 = numero_base_10 // 2
    
    # aggiunge uno 0 iniziale perché il numero è positivo
    risultato = "0" + risultato
    return risultato
    
main()
    