
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

lista.insert(1, "adios")
print(lista)

'''
dni = input("Pon tu DNI\n")

if dni.isdigit() and len(dni) == 8:
    dni = int(dni)
    nDni = dni%23
    lDni = ["T", "R", "W", "A", "G", "M", "Y", "F", "P", "D", "X", "B", "N", "J", "Z", "S", "Q", "V", "H", "L", "C", "K", "E"]
    print("Tu DNI es:", dni, "-",lDni[nDni])
    lDni.append("Tolo")
    print(lDni)
else:
    print("DNI incorrecto")
'''