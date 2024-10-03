##
#  Questo programma calcola il volume (in litri) di una confezione
# di bibite con sei lattine, seguito dal volume di una tale confezione
# insieme a una bottiglia da due litri.

# Litri in una lattina da 12 once e in una bottiglia da due litri.
CAN_VOLUME = 0.355
BOTTLE_VOLUME = 2

# Numero di lattine in una confezione.
cansPerPack = 6

# Calcoliamo il volume totale nelle lattine di una confezione.
totalVolume = cansPerPack * CAN_VOLUME
print("A six-pack of 12-ounce cans contains", totalVolume, "liters.")

# Calcoliamo il volume totale di una confezione e di una bottiglia.
totalVolume = totalVolume + BOTTLE_VOLUME
print("A six-pack and a two-liter bottle contain", totalVolume, "liters.")
