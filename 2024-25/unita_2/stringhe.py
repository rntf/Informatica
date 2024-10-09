stringa1 = "questa è una stringa"
stringa2 = 'anche questa è una stringa'

lunghezza1 = len(stringa1)
lunghezza2 = len(stringa2)

stringa_lunghezza1 = str(lunghezza1)
intero_lunghezza1 = int(stringa_lunghezza1)
float_lunghezza1 = float(stringa_lunghezza1)


stringa3 = "l'albero è verde"
stringa3 = 'l\'albero è verde'
stringa4 = 'Io dico: "Ciao!"'
stringa4 = "Io dico: \"Ciao!\""

stringa1_2 = stringa1 + " " + stringa2
# Le tre istruzioni seguenti stampano lo stesso messaggio
print(stringa1_2)
print(stringa1 + " " + stringa2)
print(stringa1, stringa2)

# per stampare su più righe
#print(stringa1)
#print(stringa2)
print("\n" + stringa1 + "\n" + stringa2)

tabulazione = "c\td"
tabulazione2 = "ab\tef"
print(tabulazione)
print(tabulazione2)

print(stringa1 * 6)