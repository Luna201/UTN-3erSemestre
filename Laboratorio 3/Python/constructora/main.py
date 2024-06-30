import cotizacionV

def ir_main():
    while True:
        try:
            opcion = int(input("""
        ++   Bienvenido a Constructora Byte-Busters   ++
Seleccione el tamaño de la construcción:
(1) - Inicio
(2) - Nosotros
(3) - Cotización
(4) - Tipología
(5) - Contáctanos
(6) - Salir
                """))
            if opcion == 1:
                print('Has seleccionado la opción 1')
            elif opcion == 2:
                print('Has seleccionado la opción 2')
            elif opcion == 3:
                cotizacionV.ir_cotizacion()
            elif opcion == 6:
                print('Saliendo del programa...')
                break
            else:
                print("Elige una opción válida.")
        except ValueError:
            print("Error: Debes ingresar un número válido.")
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")

if __name__ == "__main__":
    ir_main()



