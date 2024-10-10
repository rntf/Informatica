##
#  Calcola lo sconto per un determinato acquisto.
#

# Acquisisce il prezzo originale.
original_price = float(input("Original price before discount: "))

# Determina la percentuale di sconto da applicare.
if original_price < 128:
    discount_rate = 0.92
else:
    discount_rate = 0.84

# Calcola e visualizza il prezzo scontato.
discounted_price = discount_rate * original_price
print(f"Discounted price: {discounted_price:.2f}")
