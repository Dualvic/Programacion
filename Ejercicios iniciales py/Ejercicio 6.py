# Escribe un programa que pida por teclado dos valores de tipo numérico que se han de guardar
# en sendas variables. ¿Qué instrucciones habría que utilizar para intercambiar su contenido?
# (es necesario utilizar una variable auxiliar).
# Para comprobar que el algoritmo ideado es correcto, muestra en pantalla el contenido de las variables una vez leídas,
# y vuelve a mostrar su contenido una vez hayas intercambiado sus valores.

valorx = int(input("escribe un valor: "))
valory = int(input("Escribe un valor: "))

valorx = valory
valory = valorx

# No es necesario instalar una variable auxiliar

print valorx
print valory
