# LETTURA FILE DI TESTO
# apro il file
input_file = open("hello_world.txt", "r")


# leggo una riga del file
#riga1 = input_file.readline()
#riga1 = riga1.strip()
#print(riga1)

# leggo una seconda riga del file
#riga2 = input_file.readline()
#print(riga2)

# leggo la terza riga del file
#riga3 = input_file.readline()
#print(riga3)

# leggo tutte le righe del file
riga = input_file.readline().rstrip("\n")
while riga != "":
    print(riga)
    riga = input_file.readline().rstrip("\n")

# chiudo il file
input_file.close()

# SCRITTURA FILE DI TESTO
# apro il file
output_file = open("le mie memorie.txt", "a")

# scrivo una riga
output_file.write("Era una notte buia e tempestosa...")

# chiudo il file
output_file.close()