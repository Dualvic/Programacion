# Diseña un programa que calcule el importe final de una venta considerando
# que sobre el valor bruto se hace un descuento según la siguiente tabla:
# Valores <=20 implican un descuento del 0%
# Valores >20 y <=100 implican un descuento descuento del 5%
# Valores >100 implican un descuento 10%

valorbruto = int(input("Introduce el valor bruto: "))

if valoBruto <= 20:
    valorfinal = valorbruto
    print (valorfinal)

elif valorBruto > 20 and valorbruto <= 100:
    descuento = valorbruto * 5 / 100
    valorfinal = valorbruto - descuento
    print (valorfinal)

elif valorBruto > 100:
    descuento = valorbruto * 10 / 100
    valorfinal = valorbruto - descuento
    print (valorfinal)

else:
    print valorbruto
