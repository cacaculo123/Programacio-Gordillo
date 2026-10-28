n1 = input("Pon un numero\n")
n2 = input("Pon otro numero\n")



if n1.isdigit() and n2.isdigit():
    n1 = int(n1)
    n2 = int(n2)
    operacion = input("Que operacion quieres hacer? (suma, resta, multiplicacion, division, division entera, potencia, modúl)\n")
    #Suma
    if operacion == "suma":
        print("La suma de los dos numeros es:", n1+n2)

    #Resta
    elif operacion == "resta":
       resta = input("Quieres restar el primer numero del segundo o al reves? (1 o 2)\n")
       if resta == "1":
           print("La resta de los dos numeros es:", n1-n2)
       elif resta == "2":
           print("La resta de los dos numeros es:", n2-n1)
       else:
           print("Opción no válida")
    #Multiplicación
    elif operacion == "multiplicacion":
        print("La multiplicacion de los dos numeros es:", n1*n2)

    #Division
    elif operacion == "division":
        divison = input("Quieres dividir el primer numero del segundo o al reves? (1 o 2)\n")
        if divison == "1":
            print("La division de los dos numeros es:", n1/n2)
        elif divison == "2":
             print("La division de los dos numeros es:", n2/n1)
        else:
            print("Opción no válida")

    #Division entera
    elif operacion == "division entera":
        divison_entera = input("Quieres dividir el primer numero del segundo o al reves? (1 o 2)\n")
        if divison_entera == "1":
            print("La division entera de los dos numeros es:", n1//n2)
        elif divison_entera == "2":
             print("La division entera de los dos numeros es:", n2//n1)
        else:
            print("Opción no válida")

    #Potencia
    elif operacion == "potencia":
        print("La potencia de los dos numeros es:", n1**n2)

    #Modulo
    elif operacion == "modulo":
        print("El modulo de los dos numeros es:", n1%n2)

    
else:
    print("Los valores introducidos no son correctos")



'''
if (n1+n2) > 10: 
    print("El primer numero es mayor que el segundo")
            else:
                print("Opción no válida")
else:
    print("Los valores introducidos no son correctos")


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






