##
#  Questo programma calcola informazioni relative a una sequenza
#  di voti fornita dall’utente: il numero di voti sufficienti e
#  insufficienti, il voto medio e i voti massimo e minimo.
#

# Inizializza le variabili usate come contatore.
num_passing = 0
num_failing = 0

# Inizializza le variabili usate per calcolare la media.
total = 0
count = 0

# Inizializza le variabili per il voto minimo e massimo.
min_grade = 100.0  # Ipotizza che 100 sia il massimo voto possibile.
max_grade = 0.0

# Legge con un ciclo controllato da evento, con predisposizione.
grade = float(input("Enter a grade or -1 to finish: "))
while grade >= 0.0:
    # Incrementa il contatore di voti sufficienti o insufficienti.
    if grade >= 60.0:
        num_passing = num_passing + 1
    else:
        num_failing = num_failing + 1

    # Determina se il voto è il nuovo massimo o minimo.
    if grade < min_grade:
        min_grade = grade
    if grade > max_grade:
        max_grade = grade

    # Aggiunge il voto alla somma totale.
    total = total + grade
    count = count + 1

    # Legge il voto successivo.
    grade = float(input("Enter a grade or -1 to finish: "))

# Visualizza i risultati.
if count > 0:
    average = total / count
    print(f"The average grade is {average:.2f}")
    print(f"Number of passing grades is {num_passing}")
    print(f"Number of failing grades is {num_failing}")
    print(f"The maximum grade is {max_grade:.2f}")
    print(f"The minimum grade is {min_grade:.2f}")
