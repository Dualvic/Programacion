# Hacer un programa que dado un número de DNI obtenga la letra del NIF.

letras = "TRWAGMYFPDXBNJZSQVHLCKE"

DNI = int(input("introduce los digitos de tu DNI"))

assert len(DNI) == 8

resto = DNI % 23

print ("La letra es:",(letras[resto]))
