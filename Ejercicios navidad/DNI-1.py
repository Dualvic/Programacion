'''Verificar si una cadena de texto leída por teclado es un  DNI correcto o no.
Suponer que los DNI tienen 8 dígitos y a continuación una letra mayúscula'''

dni = ""

def solicitarDni(dni):
    nuevoDni = str(input("Introduce tu DNI: "))
	return NuevoDni

def checkDNI(dni):

    dniCorrecto = False
    while (dniCorrecto != True):
        if dni[0:8].isdigit() and dni[8].isupper():
            dniCorrecto = True
            print("El DNI es correcto")
            return True
        else:
        	print("El DNI no es valido")
        	dni=solicitarDni(dni)

dni=solicitarDni(dni)
checkDNI(dni)

###  CASOS TEST  ###

## Caso 1

# dni = "43271235A"
# > El DNI es correcto

## Caso 2

# dni = "346"
# > El DNI no es valido
# > Introduce un DNI:


## Caso 3

# dni = "asd56432R"
# > El DNI no es valido
# > Introduce un DNI:

## Caso 4

# dni ="$%!·!%/!·"
# > El DNI no es valido
# > Introduce un DNI:
