from object import ConsolaVideojuegos

def mostrar_menu():
    print("\n" + "="*40)
    print("GESTIÓN DE CONSOLA DE VIDEOJUEGOS")
    print("="*40)
    print("1. Encender/Apagar consola")
    print("2. Instalar juego")
    print("3. Verificar capacidad")
    print("4. Calcular precio por GB")
    print("5. Ver información")
    print("0. Salir")
    print("="*40)

def crear_consola():
    print("\nCREAR CONSOLA")
    marca = input("Marca: ")
    modelo = input("Modelo: ")
    
    while True:
        try:
            almacenamiento = int(input("Almacenamiento (GB): "))
            if almacenamiento > 0:
                break
            print("Debe ser mayor a 0")
        except ValueError:
            print("Ingresa un número válido")
    
    while True:
        try:
            precio = float(input("Precio: $"))
            if precio > 0:
                break
            print("Debe ser mayor a 0")
        except ValueError:
            print("Ingresa un número válido")
    
    return ConsolaVideojuegos(marca, modelo, almacenamiento, precio)

def instalar_juego_menu(consola):
    nombre = input("Nombre del juego: ")
    
    while True:
        try:
            tamaño = int(input("Tamaño (GB): "))
            if tamaño > 0:
                break
            print("Debe ser mayor a 0")
        except ValueError:
            print("Ingresa un número válido")
    
    consola.instalar_juego(nombre, tamaño)

def main():
    print("Bienvenido al Sistema de Consola de Videojuegos")
    consola = crear_consola()
    print(f"\nConsola creada:")
    print(consola)
    
    while True:
        mostrar_menu()
        
        try:
            opcion = int(input("\nSelecciona una opción: "))
            
            if opcion == 0:
                print("¡Hasta luego!")
                break
            elif opcion == 1:
                consola.encender()
            elif opcion == 2:
                instalar_juego_menu(consola)
            elif opcion == 3:
                consola.verificar_capacidad()
            elif opcion == 4:
                consola.calcular_precio_por_gb()
            elif opcion == 5:
                print(f"\n{consola}")
                print(f"Cantidad de juegos: {len(consola)}")
            else:
                print("Opción no válida")
                
        except ValueError:
            print("Ingresa un número válido")
        
        input("\nPresiona Enter para continuar...")

if __name__ == "__main__":
    main()