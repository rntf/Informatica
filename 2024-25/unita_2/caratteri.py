stringa = "questa è una stringa"
iniziale = stringa[0]
finale = stringa[len(stringa) - 1]
print(iniziale, finale)

print(stringa[3:11])
print(stringa[3:11:3])

# indici negativi
print(stringa[-2:-7:-1])

# stampo l'intera stringa al contrario
print(stringa[-1:-1 - len(stringa):-1])
print(stringa[::-1])

# carattere al di fuori della stringa
#sconosciuto = stringa[len(stringa)]
