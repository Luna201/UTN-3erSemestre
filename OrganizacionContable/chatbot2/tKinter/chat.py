def ir_chat():

    while True:
        try:
            opcion = int(input("""
            ++   Bienvenido a Byte Busters Travels   ++
    ¿Sobre que desea consultar?:
    (1) - Grupos A, B, C y D
    (2) - Fecha de Partidos 
    (3) - Lugar de Partidos
    (4) - Planes de pago
    (5) - Salir
                    """))
            if opcion == 1:
                grupo = int(input("""
                    ---     ¿ Sobre cúal grupo quiere consultar?     ---
                    (1) Grupo A: Argentina - Perú - Chile - Canada
                    (2) Grupo B: México - Ecuador - Venezuela - Jamaica
                    (3) Grupo C: Estados Unidos - Uruguay - Panamá - Bolivia
                    (4) Grupo D: Brasil - Colombia - Costa Rica - Paraguay 
                    (5) Ir a MENÚ
                    (6) SALIR
                    """))
                if grupo == 1:
                    a = int(input("""
                        ---     ¿ Que quiere consultar?     ---
                         
                        (5) Ir a MENÚ
                        (6) SALIR
                        """))

                elif grupo == 2:
                    print('Has seleccionado la opción 2')
                elif grupo == 3:
                    print(" ")
                elif grupo == 4:
                    print(' ')
                elif grupo == 5:
                    ir_chat()
                elif grupo == 6:
                    print('Saliendo del programa...')
                    break
                else:
                    print("Elige una opción válida.")

            elif opcion == 2:
                b = int(input("""
            ---     ¿ Que fecha quiere consultar?     ---
            (1) Fecha 1: Argentina vs Canada / Peru vs Chile / México vs Jamaica / Ecuador vs Venezuela
            (2) Fecha 2: 
            (3) 
            (4) 
            (5) Ir a MENÚ
            (6) SALIR
            """))
                if b == 1:
                    print(" ")
                elif b == 2:
                    print('Has seleccionado la opción 2')
                elif b == 3:
                    print(" ")
                elif b == 4:
                    print(' ')
                elif b == 5:
                    ir_chat()
                elif b == 6:
                    print('Saliendo del programa...')
                    break
                else:
                    print("Elige una opción válida.")

            elif opcion == 3:
                print(" ")
            elif opcion == 4:
                print(" ")
            elif opcion == 5:
                print('Saliendo del programa...')
                break
            else:
                print("Elige una opción válida.")
        except ValueError:
            print("Error: Debes ingresar un número válido.")
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")
