from operator import itemgetter

campo1 = ['B', 'A', 'D', 'C']
campo2 = [4, 3, 1, 2]
lista = []
for x in campo1:
    for y in campo2:
        lista.append([x, y])

print("Ordinamento sul primo campo")
lista_ordinata1 = sorted(lista)
print(lista_ordinata1)

print("Ordinamento sul secondo campo")
lista_ordinata2 = sorted(lista, key=itemgetter(1))
print(lista_ordinata2)

print("Ordinamento sul secondo campo e a parità, ordinamento sul primo")
lista_ordinata3 = sorted(lista, key=itemgetter(0))  # key=itemgetter(0) è superfluo
lista_ordinata3 = sorted(lista_ordinata3, key=itemgetter(1))
print(lista_ordinata3)

# alternativa
print("Ordinamento sul secondo campo e a parità, ordinamento sul primo")
lista_ordinata4 = sorted(lista, key=itemgetter(1, 0))
print(lista_ordinata4)