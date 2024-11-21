giorni = ['Lunedì', 'Martedì', 'Mercoledì', 'Giovedì', 'Venerdì', 'Sabato', 'Domenica']

lunghezza_lavorativi = []
for giorno in giorni:
    if giorno[-1] == "ì":
        lunghezza_lavorativi.append(len(giorno))

lunghezza = [len(giorno) for giorno in giorni if giorno[-1] == "ì"]
lunghezza_tupla = tuple(len(giorno) for giorno in giorni if giorno[-1] == "ì")
print(lunghezza_tupla) # [6, 7, 9, 7, 7, 6, 8]