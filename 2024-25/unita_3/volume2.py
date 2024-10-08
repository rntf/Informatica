##
#  Visualizza il prezzo per oncia di una confezione di sei lattine.
#

# Definisce una constante per la dimensione della confezione.
CANS_PER_PACK = 6

# Acquisisce il prezzo per confezione e il volume di una lattina.
user_input = input("Please enter the price for a six-pack: ")
pack_price = float(user_input)

user_input = input("Please enter the volume for each can (in ounces): ")
can_volume = float(user_input)

# Calcola il volume di una confezione. 
pack_volume = can_volume * CANS_PER_PACK

# Calcola e visualizza il prezzo per oncia.
price_per_ounce = pack_price / pack_volume

print(f'Price per ounce: {price_per_ounce:8.2f}')  # usa f-string
print('Price per ounce: %8.2f' % price_per_ounce)  # usa l'operatore di formattazione %

