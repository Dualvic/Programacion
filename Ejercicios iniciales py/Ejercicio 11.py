# Escribe un programa que pida por teclado tres valores de tipo entero,
# y que calcule si se cumple que la suma de dos de ellos es igual al tercero.
# La salida del programa tiene que tener el formato:
# Números introducidos: N1	N2 N3 (tabulador)

a = int(input("Escribe un numero: "))
b = int(input("Escribe un numero: "))
c = int(input("Escribe un numero: "))

if (a + b) == c:
    print ("la suma de a y b es igual a c")

elif (a + c) == b:
    print ("la suma de a y c es igual a b")

elif (c + b) == a:
    print ("la suma de b y c es igual a a")

else:
    print "no se cumple"
