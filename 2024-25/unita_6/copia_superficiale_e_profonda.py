from copy import deepcopy
table = [ [1, 2], [2, 3], [3, 4]]
#table2 = table  # table2 è un alias
#table2 = list(table)    # table2 è una copia superficiale
#table2 = deepcopy(table)    # table2 è una copia profonda

# alternativa per deep copy
table2 = []
for element in table:
    copia_elemento = list(element)
    table2.append(copia_elemento)

table2.append([5, 6])
table2[2] = [-1, 9]
table2[1][1] = 100