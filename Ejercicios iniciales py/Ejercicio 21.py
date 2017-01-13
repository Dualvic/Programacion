# Escribe 	un programa que solicite por teclado 5 números positivos,
# forzando al usuario a que únicamente introduzca valores positivos.
# A continuación el programa tiene que escribe cuál es el valor más pequeño y
# cuál es el mayor valor de los introducidos por el usuario.


## Inputs

a = int(input("Escribe un numero positivo: "))
b = int(input("Escribe un numero positivo: "))
c = int(input("Escribe un numero positivo: "))
d = int(input("Escribe un numero positivo: "))
e = int(input("Escribe un numero positivo: "))

## PreConditions
assert isinstance (a,int)
assert isinstance (b,int)
assert isinstance (c,int)
assert isinstance (d,int)
assert isinstance (e,int)
assert a >= 0 and b >= 0 and c >= 0 and d >= 0 and d >= 0

## Programa Principal

ListaNumeros = [a,b,c,d,e]

print (max(ListaNumeros))
print (min(ListaNumeros))
