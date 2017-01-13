'''6. Crea un tablero de ajedrez (matriz 8 x 8).
 Los escaques de color negro se representan por un 1 y los de color blanco con un 0.
 Muestra por pantalla el contenido de la matriz simulando un tablero de ajedrez.'''
 
matrix = []

def createMatrix(matrix):
    while len(matrix) < 8:
        matrix.append(addElement(matrix))


def addElement(matrix):
    element = []
    position = 0
    while len(element) < 9:

        if position <= 1:
          element.append(1)
          position = position + 1
        elif position >= 2 and position <= 6:
          element.append ("x")
          position = position + 1
        elif position >= 7:
          element.append(0)
          position = position + 1
        else:
            pass
    return element

def printMatrix(matrix):
  for element in matrix:
    print (element)

createMatrix(matrix)
addElement(matrix)
printMatrix(matrix)
