##
#  Questo programma visualizza la descrizione di un terremoto,
#  data la sua magnitudo sulla scala Richter
#

# Acquisisce la magnitudo dall'utente.
richter = float(input("Inserisci una magnitudo nella scala Richter: "))

# Visualizza la descrizione
if richter >= 8.0:      # gestisce il "caso speciale" per primo
    print("La maggior parte delle strutture cade")
elif richter >= 7.0:
    print("Molti edifici vengono distrutti")
elif richter >= 6.0:
    print("Molti edifici sono significativamente danneggiati e alcuni collassano")
elif richter >= 4.5:
    print("Danni a edifici costruiti in modo non adeguato")
else:                   # il "caso generale" è gestito alla fine
    print("Nessun edificio distrutto")
