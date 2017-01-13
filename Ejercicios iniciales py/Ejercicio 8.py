# Escribe un programa que pida por teclado dos números y que muestre en pantalla uno de los
# dos mensajes siguientes en función de los números leídos: a) el primer número (valor)
# es mayor que el segundo (valor)(introduciendo el valor de los números en el mensaje);
# b) el primer número (valor) es menor que el segundo (valor; c)
# los dos números son iguales (valor).

a = int(input("Escribe un numero: "))

b = int(input("Escribe un numero: "))

if a > b:
    print "a es mayor que b"
if a < b:
    print "b es mayor que a"
else a = b:
    print "Tienen el mismo valor"
