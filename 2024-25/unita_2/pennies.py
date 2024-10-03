# Converte penny in dollari e centesimi
pennies = 1729
dollars = pennies // 100  # Calcola il numero di dollari
cents = pennies % 100     # Calcola il numero di penny
print("Ho", dollars, "dollari e", cents, "centesimi")
