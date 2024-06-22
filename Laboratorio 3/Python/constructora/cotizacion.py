import main


def ir_cotizacion():
    while True:
        try:
            tamanio = int(input("""
__ Bienvenido a la sección de Cotización __
Seleccione el tamaño de la construcción:
(1) Small
(2) Medium
(3) Big
(4) Volver a MENÚ
                """))
            if tamanio == 1:
                m2 = int(input("""
            __ Seleccione el tamaño de m2: __
            (1) 45 m2
            (2) 60 m2
            (3) 75 m2
            (4) Volver a Cotización
                            """))
                if m2 == 1:
                    linea = int(input("""
                                __ Seleccione el tamaño de m2: __
                                (1) Standar ($ 299.000 el m2)
                                (2) Premium ($ 348.000 el m2)
                                (3) Country ($ 420.000 el m2)
                                (4) Volver a Cotización
                                """))
                    if linea == 1:
                        costo= 45 * 299000
                    elif linea == 2:
                        costo= 45 * 348000
                    elif linea == 3:
                        costo= 45 * 420000
                    elif linea == 4:
                        ir_cotizacion()
                    else:
                        print("Elige una opción válida.")


                elif m2 == 2:
                    print('Has seleccionado la opción 2')
                elif m2 == 3:
                    print('Has seleccionado la opción 3')
                elif m2 == 4:
                    ir_cotizacion()
                else:
                    print("Elige una opción válida.")


            elif tamanio == 2:
                print('Has seleccionado la opción 2')
            elif tamanio == 3:
                print('Has seleccionado la opción 3')
            elif tamanio == 4:
                main.ir_main()
            else:
                print("Elige una opción válida.")
        except ValueError:
            print("Error: Debes ingresar un número válido.")
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")
