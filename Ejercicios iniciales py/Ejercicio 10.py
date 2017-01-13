# Modifica el programa anterior para que en vez de mostrar un mensaje genérico en el caso
# de que alguno o los dos números sean negativos, escriba una salida diferenciada
# para cada una de las situaciones que

# se puedan producir, utilizando los siguientes mensajes:
# No se calcula la suma porque el primer número es negativo.
# No se calcula la suma porque el segundo número es negativo.
# No se calcula la suma porque los dos números son negativos.

a = int(input("Escribe un numero aqui: "))
b = int(input("Escribe un numero aqui: "))

if a > 0 and b > 0:
    print (a + b)
elif a < 0:
    print ("a es un numero negativo")
elif b < 0:
    print ("b es un numero negativo")

else a < 0 and b < 0:
    print ("ambos numeros son negativos")
