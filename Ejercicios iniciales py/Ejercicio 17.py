# Escribe 	un programa que calcule y escriba la suma de los números pares por un lado,
# y de los impares por otro, de los números comprendidos entre dos número introducidos por teclado.

primerNumero = int(input("Escribe el primero numero aqui: "))
segundoNumero = int(input("Escribe el segundo numero aqui: "))

listaPares = []
listaImpares = []
for numero in range(primerNumero,segundoNumero+1):
    if numero %2 == 0:
      listaPares.append(numero)
    else:
      listaImpares.append(numero)

sumaPares = sum(listaPares)
sumaImpares = sum(listaImpares)

print ("La suma de los pares es: ",sumaPares)
print ("La suma de los impares es: ",sumaImpares)

## Casos Test ##

# Caso Test 1

#primerNumero = 0
#segundoNumero = 10

# Caso Test 2
#primerNumero = "a"
#segundoNumero = "b"

# Caso Test 3
#primerNumero = 1
#segundoNumero = 9

# Caso Test 4
#primerNumero = 2
#segundoNumero = 12

# Caso Test 5
#primerNumero = -4
#segundoNumero = 20

# Caso Test 6
#primerNumero = -3
#segundoNumero = -16
