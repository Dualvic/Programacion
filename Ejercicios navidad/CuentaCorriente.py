class CuentaCorriente:
    def __init__(self, nombre, apellidos, direccion, telefono, nif, saldo=None):
        self.nombre = nombre
        self.apellidos = apellidos
        self.direccion = direccion
        self.telefono = telefono
        self.nif = nif
        self.saldo = saldo

    def setNombre(self,nombre):
        self.nombre = nombre

    def getNombre(self):
        return self.nombre

    def setApellidos(self, apellidos):
        self.apellidos = apellidos

    def getApellidos(self):
        return self.apellidos

    def setDireccion(self, direccion):
        self.direccion = direccion

    def getDireccion(self):
        return self.direccion

    def setTelefono(self, telefono):
        self.telefono = telefono

    def getTelefono(self):
        return self.telefono

    def setNif(self, nif):
        self.nif = nif

    def getNif (self):
        return self.nif

    def setSaldo(self, saldo):
        self.saldo = saldo

    def getSaldo(self):
        return self.saldo

    def retirarDinero(self, cantidad):
        if cantidad >= self.saldo:
            self.saldo -= cantidad
        else:
            print ("No dispones de suficiente saldo")

    def ingresarDinero(self, cantidad):
        self.saldo += cantidad

    def consultarCuenta(self,):
        nombre = " Nombre: "  + self.nombre +  " " + self.apellidos
        nif = "Identificacion: " + self.nif
        telefono = "Numero de telefono: " + self.telefono
        direccion = "Direnccion " + self.direccion
        saldo = "Saldo: " + str(self.saldo)

        print (nombre,"\n", nif, "\n", telefono,"\n", direccion,"\n" ,saldo)

    def consultarNegativo(self, saldo):
        if self.saldo < 0:
            return True
        return False


cuentaCorrienteVictor = CuentaCorriente("Victor","Garcia Regadera","calle falsa 123","637254967","12345678C",5000)

cuentaCorrienteVictor.consultarCuenta()
