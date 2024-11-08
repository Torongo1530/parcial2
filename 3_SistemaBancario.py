class CuentaBancaria:
    def __init__(self):
        self.saldoCuenta = 0

    def depositar(self, numeroCuenta):
        montoDeposito = int(input("\nIngrese la cantidad a depositar: "))
        self.saldoCuenta += montoDeposito
        print(f"\nMonto depositado en la cuenta {numeroCuenta} : {montoDeposito} Pesos\n")

    def retirar(self, numeroCuenta):
        montoRetiro = int(input(f"\nIngrese el monto a retirar de su cuenta: "))
        self.saldoCuenta -= montoRetiro
        print(f"\nMonto retirado de la cuenta {numeroCuenta}: {montoRetiro} Pesos\n")

    def obtenerSaldo(self):
        print(f"\nBalance en la cuenta: {self.saldoCuenta}\n")

class Cliente(CuentaBancaria):
    def __init__(self):
        super().__init__()
        self.listaCuentas = []
    
    def agregarCuenta(self, cuenta):
        self.listaCuentas.append(cuenta)
        print(f"Cuenta agregada: {cuenta}")

    def mostrarListaCuentas(self):
        print("\nLista de cuentas bancarias:\n")
        for i in self.listaCuentas:
            print(f"Numero de cuenta: {i}")

#Asigno el nombre al cliente
Juan = Cliente()

#Agrego los numeros de cuenta
Juan.agregarCuenta(2349792)
Juan.agregarCuenta(1231441)
Juan.agregarCuenta(2389611)

#muestro todos los numeros de cuenta
Juan.mostrarListaCuentas()

#Realizo un deposito a la segunda cuenta (1231441)
Juan.depositar(Juan.listaCuentas[1])

#Realizo un deposito a la segunda cuenta (1231441)
Juan.retirar(Juan.listaCuentas[1])

#Saldo de la cuenta
Juan.obtenerSaldo()