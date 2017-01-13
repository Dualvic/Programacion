'''El cálculo de un número elevado a otro puede hacerse de manera recursiva.
 Hacer un programa que calcule de manera recursiva cuánto vale un número x elevado a otro y.
 Los casos test pueden ser la serie del número 2 (x = 2) elevado a y,
 donde y toma los valores [0 ... 8] => 1, 2, 4, 8, 16, 32, 64, 128, 256'''

def potencia(base, exp):
    if exp == 0:
        return 1
    elif exp == 1:
        return base
    else:
        return base*potencia(base,exp-1)

print (potencia(2,5))
