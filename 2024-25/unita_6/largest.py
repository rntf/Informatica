##
#  Questo programma legge una sequenza di valori e li visualizza,
#  contrassegnando il valore massimo.
#

# Crea una lista vuota.
values = []

# Legge i valori in ingresso.
print("Please enter values, Q to quit:")
user_input = input("")
while user_input.upper() != "Q":
    values.append(float(user_input))
    user_input = input("")

# Trova il valore massimo.
largest = max(values)
# in alternativa, si può usare un ciclo
largest = values[0]
for i in range(1, len(values)):
    if values[i] > largest:
        largest = values[i]

# Visualizza tutti i valori, contrassegnando il massimo.
for element in values:
    print(element, end="")
    if element == largest:
        print(" <== largest value", end="")
    print()
