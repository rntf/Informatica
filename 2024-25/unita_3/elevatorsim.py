##
#  Questo programma simula il pannello di comando di un ascensore che salta il tredicesimo piano.
#

# Acquisisce il numero del piano come numero intero.
floor = int(input("Floor: "))

# Corregge il numero del piano, se necessario.
if floor > 13:
    actual_floor = floor - 1
else:
    actual_floor = floor

# Visualizza il risultato.
print("The elevator will travel to the actual floor", actual_floor)
