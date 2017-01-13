'''Construye un programa en el que se declare una matriz de dimensiones 5 x 8 (5 filas y 8 columnas)
 Asigna a las posiciones de la matriz números enteros generados al azar y comprendidos entre 0 y 100.
 Calcula cuál es el número más pequeño y el mayor de la tabla y muéstralos por pantalla indicando la posición que ocupan en la matriz.
 Muestra también la tabla por pantalla para comprobar los resultados.
 Para resolver este ejercicio has de importar los paquetes math y random.
 La función para generar número aleatorios se invoca: random.random()'''

from random import randint

matriz = []

def crearMatriz(matriz):
  while len(matriz) < 8:
    matriz.append(añadirElemento(matriz))


def añadirElemento(matriz):
  elementoAañadir = []
  while len(elementoAañadir) < 5:
    elemento = randint(0, 100)
    elementoAañadir.append(elemento)
  return elementoAañadir

def ordenarMatriz(matriz):
  for elemento in matriz:
    print (elemento)

def mayorMatriz(matriz):
  numeroMayor = 0

  for elemento in matriz:
    if max(elemento) > numeroMayor:
      numeroMayor = max(elemento)
    else:
      pass
  print ("el numero mayor es ", numeroMayor)

def menorMatriz(matriz):
  numeroMenor = 100
  for elemento in matriz:
    if min(elemento) < numeroMenor:
      numeroMenor = min(elemento)
    else:
      pass
  print ("el numero menor es ", numeroMenor)

def posicionMayor(matriz):
    numeroMayor = 0
    for elemento in matriz:
        if max(elemento) > numeroMayor:
          numeroMayor = max(elemento)
          posicionLista = elemento.index(numeroMayor)
          posicionElemento = matriz.index(elemento)
        else:
          pass
    print ("la posicion del numero menor es ", posicionElemento, posicionLista)

def posicionMenor(matriz):
    numeroMenor = 0
    for elemento in matriz:
        if min(elemento) > numeroMenor:
          numeroMenor = min(elemento)
          posicionLista = elemento.index(numeroMenor)
          posicionElemento = matriz.index(elemento)
        else:
          pass
    print ("la posicion del numero menor es ", posicionElemento, posicionLista)

crearMatriz(matriz)
ordenarMatriz(matriz)
mayorMatriz(matriz)
menorMatriz(matriz)
posicionMayor(matriz)
posicionMenor(matriz)
