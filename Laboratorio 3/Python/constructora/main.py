import cotizacion

def ir_main():
    while True:
        try:
            opcion = int(input("""
++   Bienvenido a Constructora Byte-Busters   ++
Seleccione el tamaño de la construcción:
(1) - 1
(2) - 2
(3) - Cotización
(4) - Salir
                """))
            if opcion == 1:
                print('Has seleccionado la opción 1')
            elif opcion == 2:
                print('Has seleccionado la opción 2')
            elif opcion == 3:
                cotizacion.ir_cotizacion()
            elif opcion == 4:
                print('Saliendo del programa...')
                break
            else:
                print("Elige una opción válida.")
        except ValueError:
            print("Error: Debes ingresar un número válido.")
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")



