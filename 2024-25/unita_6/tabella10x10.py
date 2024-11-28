def stampa_tabella(tabella):
    for i in range(len(tabella)):
        num_colonne = len(tabella[i])
        for j in range(num_colonne - 1):
            print(f"{tabella[i][j]:2d}, ", end="")
        print(tabella[i][num_colonne - 1])


tabella = []
righe = 10
colonne = 10
for i in range(righe):
    lista = []
    for j in range(colonne):
        lista.append(i * 10 + (j + 1))
    tabella.append(lista)

tabella_inversa = sorted(tabella, reverse=True)
stampa_tabella(tabella_inversa)