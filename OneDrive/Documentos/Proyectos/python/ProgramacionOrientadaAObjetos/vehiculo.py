class vehiculo:
    
    def __init__(self, Marca, Modelo, Patente, Kilometraje):
        Marca:str
        Modelo:int
        Patente:str
        Kilometraje:int
        
        self.Marca = Marca
        self.Modelo = Modelo
        self.Patente = Patente
        self.Kilometraje = Kilometraje
        
        @property
        def Marca(self):
            return self.Marca
        Marca.setter
        def Marca(self, Marca):
            self.Marca = Marca
        @property
        def Modelo(self):
            return self.__Modelo
        Modelo.setter
        def Modelo(self, Modelo):
            self.Modelo = Modelo
            
        @property
        def Patente(self):
            return self.Patente
        
        Patente.setter
        def Patente(self, Patente):
            self.Patente = Patente
        @property
        def Kilometraje(self):
            return self.Kilometraje
        
        Kilometraje.setter
        def Kilometraje(self, Kilometraje):
            self.Kilometraje = Kilometraje
    def __str__(self):
        return f"Marca: {self.Marca}, Modelo: {self.Modelo}, Patente: {self.Patente}, Kilometraje: {self.Kilometraje}"
    
vehiculo=vehiculo("hyundai",2020,"QRTU",20000)

print(vehiculo)