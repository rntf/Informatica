##
#  Questo programma confronta numeri usando espressioni booleane.
#

x = float(input("Enter a number (such as 3.5 or 4.5): "))
y = float(input("Enter a second number: "))

if x == y:
    print("They are the same.")
else:
    if x > y:
        print("The first number is larger")
    else:
        print("The first number is smaller")

    if -0.01 < x - y and x - y < 0.01:
        print("The numbers are close together")

    if -0.01 < x - y < 0.01:  # stesso confronto
        print("The numbers are close together")

    if x > 0 and y > 0 or x < 0 and y < 0:
        print("The numbers have the same sign")
    else:
        print("The numbers have different signs")
