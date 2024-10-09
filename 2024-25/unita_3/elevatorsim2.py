##
#  Questo programma simula il pannello di comando di un ascensore 
#  che salta il tredicesimo piano, con verifica del dato ricevuto.
#

# Acquisisce il numero del piano come stringa.
user_input = input("Floor: ")
if user_input.isdigit():
    floor = int(user_input)
    # Controlla che il dato ricevuto sia valido.
    if floor == 13:
        print("Error: There is no thirteenth floor.")
    elif floor <= 0 or floor > 20:
        print("Error: The floor must be between 1 and 20.")
    else:
        # Ora sappiamo che il dato è valido.
        actual_floor = floor
        if floor > 13:
            actual_floor = floor - 1
        print("The elevator will travel to the actual floor", actual_floor)

else:
   print("Error: the input is not numeric")


