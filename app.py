class Usuario:
    def __init__ (self, nombre, apellido, cedula, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula
        self.edad = edad

    
class Cuenta(Usuario):
    def __init__(self, nombre, apellido, cedula, edad, saldo = 0):
        super().__init__(nombre, apellido, cedula, edad)
        self.saldo = saldo

    def setSaldo(self, saldo):
        self.saldo = saldo
    
    def getSaldo(self):
        return self.saldo

    def depositar(self, monto):
        if monto > 0:
            self.saldo += monto
            return True
        return False

    def retirar(self, monto):
        if monto > 0 and monto <= self.saldo:
            self.saldo -= monto
            return True
        return False

    def info(self):
        return f"Nombre: {self.nombre} {self.apellido} \nCedula: {self.cedula} \nEdad: {self.edad} \nSaldo: {self.saldo}"

class Beneficio(Cuenta):
    def __init__(self, nombre, apellido, cedula, edad, saldo = 0):
        super().__init__(nombre, apellido, cedula, edad, saldo)

    def validarEdad(self, edad):
        if 18 <= edad <= 28:
            return True
        return False

    def mostrar(self):
        interes = self.saldo * 0.05
        print(super().info())
        print(f"Saldo: {self.saldo} \nTotal: {self.saldo + interes}")



if __name__ == "__main__":
    beneficio = Beneficio("Juan", "Perez", "123456789", 13, 1000)
    beneficio.mostrar()
