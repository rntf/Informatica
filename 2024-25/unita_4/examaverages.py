##
#  Questo programma calcola il voto medio per più studenti.
#

# Leggi il numero di voti per ciascuno studente.
num_exams = int(input("How many exam grades does each student have? "))

# Initializza more_grades ad un valore diverso dalla sentinella.
more_grades = "Y"

# Calcola voti medi finché l’utente non dice di smettere.
while more_grades == "Y":

    # Calcola il voto medio per uno studente.
    print("Enter the exam grades.")
    total = 0
    for i in range(1, num_exams + 1):
        score = int(input(f"Exam {i}: "))	  # Chiedi il voto di ogni esame.
        total = total + score

    average = total / num_exams
    print(f"The average is {average:.2f}")

    # Chiedi all’utente se vuole calcolare il voto medio di un altro studente.
    more_grades = input("Enter exam grades for another student (Y/N)? ")
    more_grades = more_grades.upper()
