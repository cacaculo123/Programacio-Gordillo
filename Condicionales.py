n1 = input("Posa un numero\n")
n2 = input("Posa un altres numero\n")



if n1 and n2 == int:
    operacion = input("Que operacion quieres hacer? (suma, resta, multiplicacion, division, division entera, potencia, modúl)\n")
    if operacion == "suma":
        print("La suma de los dos numeros es:", n1+n2)
    elif operacion == "resta":
        print("La resta de los dos numeros es:", n1-n2, "o", n2-n1)
    elif operacion == "multiplicacion":
        print("La multiplicacion de los dos numeros es:", n1*n2)
    elif operacion == "division":
        print("La division de los dos numeros es:", n1/n2, "o", n2/n1)
    elif operacion == "division entera":
        print("La division entera de los dos numeros es:", n1//n2, "o", n2//n1)
    elif operacion == "potencia":
        print("La potencia de los dos numeros es:", n1**n2)
    elif operacion == "modulo":
        print("El modulo de los dos numeros es:", n1%n2)
else:
    print("Los valores introducidos no son correctos")



'''
if (n1+n2) > 10: 
    print("El primer numero es mayor que el segundo")
else:
    print("El primer numero es menor que el segundo")



if (n1+n2 > 8 or n1+n2 < 4): 
    print("La suma de los dos numeros es mayor que 8 o es menor a 4")

if (n1+n2 > 12 or n1+n2 < 18): 
    print("La suma de los dos numeros es mayor que 14 o es menor que 18")

if not (n1 + n2 == 13):
    print("La suma de los dos numeros no es igual a 13")
elif (n1 + n2 == 15):
    print("La suma de los dos numeros es igual a 15")

'''





