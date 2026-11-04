lista = [2, "hola", 3.5]

print(lista[0])
print(lista[1])
print(lista[2])

print(lista)
print (len(lista))

llista = lista + [4, 6, 9]

print(llista[0:3])

lista[2] = "bah"
print(lista)

del lista[1]
print(lista)

lista[2] = ""
print(lista)