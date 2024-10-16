massimo = max(4, 6, 7, 3, 5, -1, -5)
valore = print("Hello world")
if valore:
    print("Valore restituito")
else:
    print("Nessun valore")

temperatura_stringa = input("Introduci la temperatura: ")
if temperatura_stringa.isdigit():
    temperatura = int(temperatura_stringa)

    liquido = temperatura > 0 and temperatura < 100
    #if temperatura > 0 and temperatura < 100:
    if liquido:
        print("Acqua allo stato liquido")
    else:
        if temperatura <= 0:
            print("Acqua ghiacciata")
        else:
            print("Acqua allo stato gassoso")

    ghiacciato = (temperatura <= 0)
    # equivalente con elif
    if liquido:
        print("Acqua allo stato liquido")
    elif ghiacciato:
        print("Acqua ghiacciata")
    else:
        print("Acqua allo stato gassoso")

    if temperatura > 0:
        print("liquido o gas")

    # equivalente?
    if temperatura:
        print("liquido o gas")

else:
    print("Introduci un valore numerico")