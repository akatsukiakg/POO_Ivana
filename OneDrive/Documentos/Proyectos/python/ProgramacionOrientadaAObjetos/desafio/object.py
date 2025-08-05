class ConsolaVideojuegos:
    def __init__(self, marca, modelo, almacenamiento_gb, precio):
        self.marca = marca
        self.modelo = modelo
        self.almacenamiento_gb = almacenamiento_gb
        self.precio = precio
        self.juegos_instalados = []
        self.espacio_usado = 0
        self.encendida = False
    
    def instalar_juego(self, nombre_juego, tamaño_gb):
        if not self.encendida:
            print("La consola debe estar encendida")
            return False
            
        if self.espacio_usado + tamaño_gb > self.almacenamiento_gb:
            print(f"No hay espacio suficiente. Necesitas {tamaño_gb} GB")
            return False
            
        self.juegos_instalados.append(nombre_juego)
        self.espacio_usado += tamaño_gb
        print(f"Juego '{nombre_juego}' instalado correctamente")
        return True
    
    def calcular_precio_por_gb(self):
        if self.almacenamiento_gb > 0:
            precio_por_gb = self.precio / self.almacenamiento_gb
            print(f"Precio por GB: ${precio_por_gb:.2f}")
            return precio_por_gb
        return 0
    
    def verificar_capacidad(self):
        espacio_libre = self.almacenamiento_gb - self.espacio_usado
        porcentaje_usado = (self.espacio_usado / self.almacenamiento_gb) * 100
        
        if porcentaje_usado >= 90:
            estado = "CRÍTICO"
        elif porcentaje_usado >= 70:
            estado = "ALTO"
        else:
            estado = "NORMAL"
            
        print(f"Espacio usado: {self.espacio_usado} GB ({porcentaje_usado:.1f}%)")
        print(f"Espacio libre: {espacio_libre} GB")
        print(f"Estado del almacenamiento: {estado}")
        return estado
    
    def encender(self):
        self.encendida = not self.encendida
        estado = "encendida" if self.encendida else "apagada"
        print(f"Consola {estado}")
    
    def __str__(self):
        estado = "Encendida" if self.encendida else "Apagada"
        return (f"Consola {self.marca} {self.modelo}\n"
                f"Almacenamiento: {self.almacenamiento_gb} GB\n"
                f"Precio: ${self.precio}\n"
                f"Juegos: {len(self.juegos_instalados)}\n"
                f"Estado: {estado}")
    
    def __len__(self):
        return len(self.juegos_instalados)
    
    def __add__(self, otra_consola):
        return self.precio + otra_consola.precio