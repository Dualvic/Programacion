# Escribe	un programa que pida por teclado dos números y que calcule y muestre su
# suma solamente si:
# los dos son pares
# el primero es menor que cincuenta
# y el segundo está dentro del intervalo cerrado 100-500.
# En el caso de que no se cumplan las condiciones, en vez de la suma ha de
# visualizarse un mensaje de error.

a = int(input("Escribe un numero: "))
b = int(input("Escribe un numero: "))

if a % 2 == 0 and b % 2 == 0 and a > 50 and b in range(100,500):
	print (a + b)
else:
    print ("No se cumplen las condiciones")
