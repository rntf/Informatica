##
#  Questo programma visualizza il valore medio di una sequenza 
#  di salari terminata da una sentinella.
#

# Inizializza le variabili per la somma e il conteggio.
total = 0.0
count = 0

# Inizializza salary a un valore che non sia una sentinella.
salary = 0.0

# Elabora i dati fino all’arrivo della sentinella.
while salary >= 0.0:
    salary = float(input("Enter a salary or -1 to finish: "))
    if salary >= 0.0:
        total = total + salary
        count = count + 1

# Calcola e visualizza il salario medio.
if count > 0:
    average = total / count
    print("Average salary is", average)
else:
    print("No data was entered.")
