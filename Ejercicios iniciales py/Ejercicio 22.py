# Repite el programa anterior, pero en vez de leer 5 números, el usuario ha
# de indicar antes cuántos números van a ser leídos, indicándolo mediante
# el mensaje: Introduzca cuántos números tienen que leerse por teclado: _

## Inputs

rangonumeros = int(input ("Introduzca cuántos números tienen que leerse por teclado: "))
ListaNumeros = []
contador = 0
while contador < rangonumeros:
    valorAintroducir = int(input("Escribe un numero aqui: "))
    ListaNumeros.append(valorAintroducir)
    contador = contador + 1

## PreConditions

assert isinstance (ListaNumeros,list), "Internal Error"
assert isinstance (valorAintroducir,int), "No es un numero"
assert len(ListaNumeros) == rangonumeros, "Valor introducido no es igual al prefijado"

## Programa Principal

if len(ListaNumeros) == rangonumeros:
    print ("El numero mas grande es", max(ListaNumeros))
    print ("El numero mas pequeño es", min(ListaNumeros))
else:
    print ("Rango introducido incorrecto")
