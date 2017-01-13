# Escribe un programa que nos pida por teclado dos números enteros y que
# a continuación muestre en pantalla la suma de los dos números solamente si
# son los dos positivos. Si no se cumple que los dos números sean positivos se
# visualizará un mensaje indicándolo. La salida ha de tener el siguiente formato:
# “La suma de los dos números es: "XXX” o “No se calcula la suma porque
# alguno de los números o los dos no son positivos”.

a = int(input("Escribe un numero aqui: "))
b = int(input("Escribe un numero aqui: "))

if a > 0 and b > 0:
    print (a + b)
else:
    print ("no son positivos")
