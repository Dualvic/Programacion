# Lee por teclado 5 números enteros positivos,
# y escribe cuál es el mayor de los números introducidos.

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

print max(ListaNumeros)
