import main


def ir_cotizacion():
    global tamanio, m2, costo, cuotas
    while True:
        try:
            tamanio = int(input("""
                __ Bienvenido a la sección de Cotización __
Seleccione el tamaño de la construcción:
 (1) Small\n (2) Medium\n (3) Big\n (4) Volver a MENÚ\n """))
            if tamanio == 1:  # OPCION SMALL
                tamanioElegido = "Small"
                m2 = int(input("""
                __ Seleccione el tamaño de m2: __
 (1) 45 m2\n (2) 60 m2\n (3) 75 m2\n (4) Volver a Cotización\n """))
                if m2 == 1:
                    m2Elegido = "45 m2"
                    linea = int(input("""
                __ Seleccione la línea que desea: __
(1) Standar ($ 299.000 el m2)\n (2) Premium ($ 348.000 el m2)\n (3) Country ($ 420.000 el m2)\n (4) Volver a Cotización\n """))
                    if linea == 1:
                        lineaElegida = "Standar"
                        costo = 45 * 299000
                    elif linea == 2:
                        lineaElegida = "Premium"
                        costo = 45 * 348000
                    elif linea == 3:
                        lineaElegida = "Country"
                        costo = 45 * 420000
                    elif linea == 4:
                        ir_cotizacion()
                    else:
                        print("Elige una opción válida.")

                elif m2 == 2:
                    m2Elegido = "60 m2"
                    linea = int(input("""
                __ Seleccione la línea que desea: __
 (1) Standar ($ 299.000 el m2)\n (2) Premium ($ 348.000 el m2)\n (3) Country ($ 420.000 el m2)\n (4) Volver a Cotización\n """))
                    if linea == 1:
                        lineaElegida = "Standar"
                        costo = 60 * 299000
                    elif linea == 2:
                        lineaElegida = "Premium"
                        costo = 60 * 348000
                    elif linea == 3:
                        lineaElegida = "Country"
                        costo = 60 * 420000
                    elif linea == 4:
                        ir_cotizacion()
                    else:
                        print("Elige una opción válida.")

                elif m2 == 3:
                    m2Elegido = "75 m2"
                    linea = int(input("""
                __ Seleccione la línea que desea: __
 (1) Standar ($ 299.000 el m2)\n (2) Premium ($ 348.000 el m2)\n (3) Country ($ 420.000 el m2)\n (4) Volver a Cotización\n """))
                    if linea == 1:
                        lineaElegida = "Standar"
                        costo = 75 * 299000
                    elif linea == 2:
                        lineaElegida = "Premium"
                        costo = 75 * 348000
                    elif linea == 3:
                        lineaElegida = "Country"
                        costo = 75 * 420000
                    elif linea == 4:
                        ir_cotizacion()
                    else:
                        print("Elige una opción válida.")

                elif m2 == 4:
                    ir_cotizacion()
                else:
                    print("Elige una opción válida.")


            elif tamanio == 2:  # OPCION MEDIUM
                tamanioElegido = "Medium"
                m2 = int(input("""
                __ Seleccione el tamaño de m2: __
 (1) 70 m2\n (2) 90 m2\n (3) 105 m2\n (4) Volver a Cotización\n """))
                if m2 == 1:
                    m2Elegido = "70 m2"
                    linea = int(input("""
                __ Seleccione la línea que desea: __
 (1) Standar ($ 299.000 el m2)\n (2) Premium ($ 348.000 el m2)\n (3) Country ($ 420.000 el m2)\n (4) Volver a Cotización\n """))
                    if linea == 1:
                        lineaElegida = "Standar"
                        costo = 70 * 299000
                    elif linea == 2:
                        lineaElegida = "Premium"
                        costo = 70 * 348000
                    elif linea == 3:
                        lineaElegida = "Country"
                        costo = 70 * 420000
                    elif linea == 4:
                        ir_cotizacion()
                    else:
                        print("Elige una opción válida.")

                elif m2 == 2:
                    m2Elegido = "90 m2"
                    linea = int(input("""
                __ Seleccione la línea que desea: __
 (1) Standar ($ 299.000 el m2)\n (2) Premium ($ 348.000 el m2)\n (3) Country ($ 420.000 el m2)\n (4) Volver a Cotización\n """))
                    if linea == 1:
                        lineaElegida = "Standar"
                        costo = 90 * 299000
                    elif linea == 2:
                        lineaElegida = "Premium"
                        costo = 90 * 348000
                    elif linea == 3:
                        lineaElegida = "Country"
                        costo = 90 * 420000
                    elif linea == 4:
                        ir_cotizacion()
                    else:
                        print("Elige una opción válida.")

                elif m2 == 3:
                    m2Elegido = "105 m2"
                    linea = int(input("""
                __ Seleccione la línea que desea: __
 (1) Standar ($ 299.000 el m2)\n (2) Premium ($ 348.000 el m2)\n (3) Country ($ 420.000 el m2)\n (4) Volver a Cotización\n """))
                    if linea == 1:
                        lineaElegida = "Standar"
                        costo = 105 * 299000
                    elif linea == 2:
                        lineaElegida = "Premium"
                        costo = 105 * 348000
                    elif linea == 3:
                        lineaElegida = "Country"
                        costo = 105 * 420000
                    elif linea == 4:
                        ir_cotizacion()
                    else:
                        print("Elige una opción válida.")

                elif m2 == 4:
                    ir_cotizacion()
                else:
                    print("Elige una opción válida.")


            elif tamanio == 3:  # OPCION BIG
                tamanioElegido = "Big"
                m2 = int(input("""
                __ Seleccione el tamaño de m2: __
 (1) 80 m2\n (2) 100 m2\n (3) 120 m2\n (4) Volver a Cotización\n """))
                if m2 == 1:
                    m2Elegido = "80 m2"
                    linea = int(input("""
                __ Seleccione la línea que desea: __
 (1) Standar ($ 299.000 el m2)\n (2) Premium ($ 348.000 el m2)\n (3) Country ($ 420.000 el m2)\n (4) Volver a Cotización\n """))
                    if linea == 1:
                        lineaElegida = "Standar"
                        costo = 80 * 299000
                    elif linea == 2:
                        lineaElegida = "Premium"
                        costo = 80 * 348000
                    elif linea == 3:
                        lineaElegida = "Country"
                        costo = 80 * 420000
                    elif linea == 4:
                        ir_cotizacion()
                    else:
                        print("Elige una opción válida.")

                elif m2 == 2:
                    m2Elegido = "100 m2"
                    linea = int(input("""
                __ Seleccione la línea que desea: __
 (1) Standar ($ 299.000 el m2)\n (2) Premium ($ 348.000 el m2)\n (3) Country ($ 420.000 el m2)\n (4) Volver a Cotización\n """))
                    if linea == 1:
                        lineaElegida = "Standar"
                        costo = 100 * 299000
                    elif linea == 2:
                        lineaElegida = "Premium"
                        costo = 100 * 348000
                    elif linea == 3:
                        lineaElegida = "Country"
                        costo = 100 * 420000
                    elif linea == 4:
                        ir_cotizacion()
                    else:
                        print("Elige una opción válida.")

                elif m2 == 3:
                    m2Elegido = "120 m2"
                    linea = int(input("""
                __ Seleccione la línea que desea: __
 (1) Standar ($ 299.000 el m2)\n (2) Premium ($ 348.000 el m2)\n (3) Country ($ 420.000 el m2)\n (4) Volver a Cotización\n """))
                    if linea == 1:
                        lineaElegida = "Standar"
                        costo = 120 * 299000
                    elif linea == 2:
                        lineaElegida = "Premium"
                        costo = 120 * 348000
                    elif linea == 3:
                        lineaElegida = "Country"
                        costo = 120 * 420000
                    elif linea == 4:
                        ir_cotizacion()
                    else:
                        print("Elige una opción válida.")

                elif m2 == 4:
                    ir_cotizacion()
                else:
                    print("Elige una opción válida.")

            elif tamanio == 4:
                main.ir_main()
            else:
                print("Elige una opción válida.")

            print(f'El costo es: $ {costo}')

            # OPCIÓN DE ENTREGAR DINERO POR ADELANTADO
            while True:
                opcionAdelanto = int(input("""
                -- Digite una opción de menú: --
 (1) SI ingresar adelanto\n (2) NO ingresar adelanto\n (3) Volver a Cotización\n """))
                if opcionAdelanto == 1:
                    adelanto = float(input("¿Cuanto dinero desea ingresar? <- "))
                    break
                elif opcionAdelanto == 2:
                    adelanto = 0
                    break
                elif opcionAdelanto == 3:
                    ir_cotizacion()
                else:
                    print("Elige una opción válida.")

            restoApagar = costo - adelanto
            print(f'$ {restoApagar}')

            while True:  # SELECCIÓN DE CUOTAS A PAGAR
                tiempoPago = int(input("""
                --¿En cuantas cuotas desea pagar?: --
 (1) 12 cuotas (0% interes)\n (2) 24 cuotas (interes: 50%)\n (3) 36 cuotas (interes: 75%)\n (4)Volver a Cotización\n """))
                if tiempoPago == 1:
                    pagoFinal = restoApagar
                    cuotas = pagoFinal / 12
                    break
                elif tiempoPago == 2:
                    pagoFinal = (restoApagar * 150) / 100
                    cuotas = pagoFinal / 24
                    break
                elif tiempoPago == 3:
                    pagoFinal = (restoApagar * 175) / 100
                    cuotas = pagoFinal / 36
                    break
                elif tiempoPago == 4:
                    ir_cotizacion()
                else:
                    print("Elige una opción válida.")

                        #PRINT PARA VER LAS OPCIONES ELEGIDAS
            print(f"""      
                --ELECCIONES REALIZADAS:
 # TAMAÑO DE CONSTRUCCIÓN: {tamanioElegido}\n # DIMENSIÓN EN m2: {m2Elegido}\n # LINEA DE CONSTRUCCIÓN: {lineaElegida}\n # IMPORTE BRUTO: ${costo}
 # ADELANTO ENTREGADO: $ {adelanto}\n # COSTO TOTAL FINAL: ${pagoFinal}, EN CUOTAS DE: ${cuotas} MENSUALES""")

            while True:     #CICLO PARA CONTINUAR O SALIR DE COTIZACIONES
                fin = int(input("""
                __ ¿Desea cotizar nuevamente?: __
 (1) Continuar\n (2) Salir a Menú principal\n """))
                if fin == 1:
                    break
                elif fin == 2:
                    main.ir_main()
                else:
                    print("Elige una opción válida.")

        except ValueError:                      #Excepcion de valor
            print("Error: Debes ingresar un número válido.")

        except Exception as e:                  #Excepcion general
            print(f"Ocurrió un error inesperado: {e}")
