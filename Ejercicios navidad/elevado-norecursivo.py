''' Resuelve el ejercicio anterior utilizando una rutina NO recursiva. '''

def potencia(base,exp):
    if exp == 0:
        return 1
    elif exp == 1:
        return base
    else:
        return base**exp

print (potencia(2,5))
