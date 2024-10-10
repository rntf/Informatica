##
#  Calcola le tasse sul reddito usando uno schema semplificato.
#

# Inizializza costanti per le aliquote e per i limiti degli scaglioni.
RATE1 = 0.10
RATE2 = 0.25
RATE1_SINGLE_LIMIT = 32000.0
RATE1_MARRIED_LIMIT = 64000.0

# Legge il reddito e lo stato civile     
income = float(input("Please enter your income: "))
marital_status = input("Please enter s for single, m for married: ")

# Calcola le tasse dovute.
tax1 = 0
tax2 = 0

if marital_status == "s":
    if income <= RATE1_SINGLE_LIMIT:
        tax1 = RATE1 * income
    else:
        tax1 = RATE1 * RATE1_SINGLE_LIMIT
        tax2 = RATE2 * (income - RATE1_SINGLE_LIMIT)
else:
    if income <= RATE1_MARRIED_LIMIT:
        tax1 = RATE1 * income
    else:
        tax1 = RATE1 * RATE1_MARRIED_LIMIT
        tax2 = RATE2 * (income - RATE1_MARRIED_LIMIT)

total_tax = tax1 + tax2

# Visualizza il risultato.
print(f"The tax is ${total_tax:.2f}")
