richter = int(input("Inserisci il grado del terremoto"))

if richter < 4.5:
    print("nessun danno")
else:
    if richter <= 5.99:
        print("danni ad edifici non adeguati")
    else:
        if richter <= 6.99:
            print("Molti edifici danneggiati")
        else:
            if richter <= 7.99:
                print("Molti edifici sono distrutti")
            else:
                print("Tutto distrutto")

# alternativa
if richter < 4.5:
    print("nessun danno")
elif richter <= 5.99:
    print("danni ad edifici non adeguati")
elif richter <= 6.99:
    print("Molti edifici danneggiati")
elif richter <= 7.99:
    print("Molti edifici sono distrutti")
else:
    print("Tutto distrutto")
