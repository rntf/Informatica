##
#  Calcola il tempo richiesto per il raddoppio di un investimento.
#

# Definisce le costanti.
RATE = 5.0
INITIAL_BALANCE = 10000.0
TARGET = 2 * INITIAL_BALANCE

# Inizializza le variabili usate nel ciclo.
balance = INITIAL_BALANCE
year = 0

# Conta gli anni richiesti per il raddoppio dell’investimento.
while balance < TARGET:
    year = year + 1
    interest = balance * RATE / 100
    balance = balance + interest

# Visualizza il risultato.   
print("The investment doubled after", year, "years.")
