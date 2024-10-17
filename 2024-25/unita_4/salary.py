total = 0.0
count = 0

salary = float(input("Inserisci salario, valore negativo per terminare: "))

while salary >= 0.0:
    total += salary
    count += 1
    salary = float(input("Inserisci salario, valore negativo per terminare: "))

print(f"Hai {count} dipendenti e ti costano {total}")


# alternativa con variabile booleana
salary = float(input("Inserisci salario, valore negativo per terminare: "))

if salary >= 0.0:
    continua = True
else:
    continua = False
while continua:
    total += salary
    count += 1
    salary = float(input("Inserisci salario, valore negativo per terminare: "))
    if salary < 0.0:
        continua = False
        