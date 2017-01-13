# Escribe un programa que pida por teclado un número y que a continuación muestre
# el mensaje el número leído es positivo o bien el número leído es negativo
# dependiendo de que el número introducido por teclado sea positivo o negativo.
# Consideramos al número 0 positivo.

def checkPositivo (a):

    if a > 0:
        return "es positivo"
    else:
        return "es negativo"

# Casos test

# Caso test 1

print checkPositivo(5)

# >> "Es positivo"

# Caso Test 2

print checkPositivo(-1)

# >> "Es negativo"
