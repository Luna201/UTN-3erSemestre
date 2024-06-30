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
            ---     ¿Que fecha quiere consultar?     ---
            (1) Fecha 1: Argentina vs Canada / Peru vs Chile / México vs Jamaica / Ecuador vs Venezuela /
                         EE.UU vs Bolivia / Uruguay vs Panamá / Brasil vs Costa Rica / Colombia vs Paraguay
            (2) Fecha 2: Argentina vs Chile / Peru vs Canada / México vs Venezuela / Ecuador vs Jamaica /
                         EE.UU vs Panamá / Uruguay vs Bolivia / Brasil vs Paraguay / Colombia vs Costa Rica
            (3) Fecha 3:Argentina vs Peru / Canada vs Chile / México vs Ecuador / Jamaica vs Venezuela /
                         EE.UU vs Uruguay / Bolivia vs Panamá / Brasil vs Colombia / Costa Rica vs Paraguay
            (4) Cuartos de Final: 1B vs 2A / 1A vs 2B / 1D vs 2C / 1C vs 2D
            (5) Semifinal: Ganador (1B vs 2A) vs Ganador (1A vs 2B) / Ganador (1D vs 2C) vs Ganador (1C vs 2D)
            (6) Final:  Final y 3er Puesto
            (7) Ir a MENÚ
            (8) SALIR
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
