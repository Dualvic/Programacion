# Escribe un programa que visualice los n-primeros múltiplos de 2,
# siendo n un valor leído por teclado.

def PrimerosMultiplos (numero):
    contador = 0
    multiplo = int(input("Escribe un numero: "))
    while contador <= multiplo:
        resultado = numero * contador
        print (resultado)
        contador = contador + 1
    return contador

print (PrimerosMultiplos(2))
