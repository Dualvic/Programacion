'''Verificar si una cadena de texto leída por teclado es un
 DNI correcto o no. Suponer que los DNI tienen 8 dígitos y
 a continuación una letra mayúscula.'''

DNI = str(input("Introduce tu DNI"))

assert isinstance (DNI,str)
assert len(DNI) == 9

letra = DNI[8]
print (letra)
