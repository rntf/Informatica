def main():
    valore_input = int(input("Inserisci un numero in cifre: "))
    valore_come_stringa = converti_in_parole(valore_input)
    print(valore_come_stringa)

def converti_in_parole(valore_numerico):
    (stringa1, valore_numerico)= converti_centinaia(valore_numerico)
    stringa2 = converti_decine_e_unita(valore_numerico)
    return stringa1 + stringa2


def converti_centinaia(valore):
    # 1) estraggo le centinaia
    # valore = 835 -> centinaia = 8
    centinaia = valore // 100

    # 2) converto cifra in lettere
    if centinaia == 1:
        lettere = "cento"
    else:
        lettere = converto_cifra_in_lettere(centinaia) + "cento"
    
    # 3) tolgo la prima cifra dal numero
    #valore = valore - centinaia * 100
    valore = valore % 100   # valore = 35
    return (lettere, valore)

def converto_cifra_in_lettere(cifra):
    if cifra == 1:
        return "uno"
    elif cifra == 2:
        return "due"
    elif cifra == 3:
        return "tre"
    elif cifra == 4:
        return "quattro"
    elif cifra == 5:
        return "cinque"
    elif cifra == 6:
        return "sei"
    elif cifra == 7:
        return "sette"
    elif cifra == 8:
        return "otto"
    elif cifra == 9:
        return "nove"


def converti_decine_e_unita(valore):
    if valore >= 20:
        (stringa1, valore) = converti_decine(valore)
        stringa2 = converto_cifra_in_lettere(valore)
        return stringa1 + stringa2
    elif valore >= 10:
        stringa = converti_10_19_in_lettere(valore)
        return stringa
    else:
        stringa = converto_cifra_in_lettere(valore)
        return stringa
    
def converti_decine(valore):
    # estraggo le decine
    # valore = 35 -> decina = 3
    decina = valore // 10
    lettere = converto_decina_in_lettere(decina)
    valore = valore % 10   # valore = 5
    return (lettere, valore)

def converto_decina_in_lettere(cifra):
    if cifra == 2:
        return "venti"
    elif cifra == 3:
        return "trenta"
    elif cifra == 4:
        return "quaranta"
    elif cifra == 5:
        return "cinquanta"
    elif cifra == 6:
        return "sesanta"
    elif cifra == 7:
        return "settanta"
    elif cifra == 8:
        return "ottanta"
    elif cifra == 9:
        return "novanta"


def converti_10_19_in_lettere(valore):
    if valore == 10:
        return "dieci"
    elif valore == 11:
        return "undici"
    elif valore == 12:
        return "dodici"
    elif valore == 13:
        return "tredici"
    elif valore == 14:
        return "quattordici"
    elif valore == 15:
        return "quindici"
    elif valore == 16:
        return "sedici"
    elif valore == 17:
        return "diciassette"
    elif valore == 18:
        return "diciotto"
    else:
        return "diciannove"
    
main()


