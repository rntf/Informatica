##
#  Questo programma visualizza una tabella che mostra.
#  la crescita di un investimento
#

# Definisce le costanti.
RATE = 5.0
INITIAL_BALANCE = 10000.0

# Legge il numero di anni per cui eseguire la simulazione.
num_years = int(input("Enter number of years: "))

# Visualizza la tabella con il saldo di ciascun anno.
balance = INITIAL_BALANCE
for year in range(1, num_years + 1):
    interest = balance * RATE / 100
    balance = balance + interest
    print(f'{year:4d} {balance:10.2f}')
