'''4.  Almacenar en un vector (una lista) 5 números enteros leídos por teclado.
 Leer a continuación otro número y comprobar si está en el vector o no.
En el caso de que esté visualizar qué posición ocupa. Sino indicarlo mediante un mensaje.
 Visualizar también el elemento más pequeño, el más grande y la posición de ambos en el vector.
'''
def encontrarPosicion(numero, vector):
    if numero in vector:
        print ("la posicion del vector es: " + str(vector.index(numero)))
    else:
        print ("El numero no esta en el vector")


def MayorMenor(vector):
    numeromenor = min(vector)
    numeromayor = max(vector)

    posicionMenor = vector.index(numeromenor)
    posicionMayor = vector.index(numeromayor)

    smallString = "El numero menor es: " + str(numeromenor) + " y su posicion es: " + str(posicionMenor)
    highString = "El numero mayor es: " + str(numeromayor) + " y su posicion es: " + str(posicionMayor)

    print (smallString,"\n", highString)


vector = []

for dato in range(0, 5):
    vector.append(int(input("Introduce un valor: ")))
print(vector)

numeroAcomprobar = int(input("Introduce el numero a comprobar: "))

encontrarPosicion(numeroAcomprobar, vector)
MayorMenor(vector)
