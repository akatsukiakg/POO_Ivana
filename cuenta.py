class Cuenta:
    def __init__(self, titular, nro_cuenta, monto):
        self._titular = titular
        self._nro_cuenta = nro_cuenta
        self._monto = monto


    def get_titular(self):
        return self._titular

    def get_nro_cuenta(self):
        return self._nro_cuenta

    def get_monto(self):
        return self._monto


    def set_titular(self, titular):
        self._titular = titular

    def set_nro_cuenta(self, nro_cuenta):
        self._nro_cuenta = nro_cuenta

  

    def mostrar(self):
        print(f"Titular: {self._titular}")
        print(f"Nro de cuenta: {self._nro_cuenta}")
        print(f"Monto: {self._monto:}")

    def ingresar(self, cantidad):
        if cantidad > 0:
            self._monto += cantidad

    def retirar(self, cantidad):
        self._monto -= cantidad
        if self._monto < 0:
            print("No se puede retirar más de lo que hay en la cuenta.")
            self._monto += cantidad
        
Cuenta = Cuenta("Juan Perez", 123456, 1000.50)
Cuenta.mostrar()
Cuenta.ingresar(500)
Cuenta.mostrar()
Cuenta.retirar(200)
Cuenta.mostrar()
Cuenta.retirar(2000)
Cuenta.mostrar()