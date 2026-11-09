n1 = input("Pon el primer numero\n")
n2 = input("Pon el segundo numero\n")
n3 = input("Pon el tercer numero\n")
n4 = input("Pon el cuarto numero\n")

if n1.replace("-", "", 1).replace(".", "", 1).isdigit() and n2.replace("-", "", 1).replace(".", "", 1).isdigit() and n3.replace("-", "", 1).replace(".", "", 1).isdigit() and n4.replace("-", "", 1).replace(".", "", 1).isdigit():
    n1 = int(n1)
    n2 = int(n2)
    n3 = int(n3)
    n4 = int(n4)

    numeros = [n1, n2, n3, n4]
    if numeros[0] > numeros[1]:
        numeros[1], numeros[2] = numeros[2], numeros[1]
    if numeros[0] > numeros[2]:
        numeros[1], numeros[3] = numeros[3], numeros[1]
    if numeros[0] > numeros[3]:
        numeros[1], numeros[4] = numeros[4], numeros[1]
 
    print("Los numeros ordenados de menor a mayor son:", numeros)
else:
    print("Los valores introducidos no son correctos")  
