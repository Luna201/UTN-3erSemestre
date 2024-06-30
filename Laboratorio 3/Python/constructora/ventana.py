import tkinter
from tkinter import *
import tkinter as tk
import main
from customtkinter import CTkButton

c_negro = "#010101"
c_morado = "#7f5af0"
c_verde = "#2cb67d"
c_azul = "#33DDFF"
c_azulOscuro = "#2980B9"
c_blanco = "#FFFFFF"
c_azulClaro = "#86A9FD"

global ventana
ventana = tkinter.Tk()
ancho_pantalla = ventana.winfo_screenwidth()
altura_pantalla = ventana.winfo_screenheight()
ancho_ventana = int(ancho_pantalla)
altura_ventana = int(altura_pantalla)
ventana.geometry(f"{ancho_ventana}x{altura_ventana}")
ventana.config()
ventana.title("Sistema de control de facturas")

label_inicio = tk.Label(ventana, text="---   Cotización   ---", bd=2, fg="black", font=("Verdana", 18))
label_inicio.pack(pady=20)

#
def ir_cotizacion():
    global tamanio, m2, costo

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

                    # PRINT PARA VER LAS OPCIONES ELEGIDAS
            print(f"""      
                --ELECCIONES REALIZADAS:
 # TAMAÑO DE CONSTRUCCIÓN: {tamanioElegido}\n # DIMENSIÓN EN m2: {m2Elegido}\n # LINEA DE CONSTRUCCIÓN: {lineaElegida}\n # IMPORTE BRUTO: ${costo}
 # ADELANTO ENTREGADO: $ {adelanto}\n # COSTO TOTAL FINAL: ${pagoFinal}, EN CUOTAS DE: ${cuotas} MENSUALES""")

            while True:  # CICLO PARA CONTINUAR O SALIR DE COTIZACIONES
                fin = int(input("""
                __ ¿Desea cotizar nuevamente?: __
 (1) Continuar\n (2) Salir a Menú principal\n """))
                if fin == 1:
                    break
                elif fin == 2:
                    main.ir_main()
                else:
                    print("Elige una opción válida.")

        except ValueError:  # Excepcion de valor
            print("Error: Debes ingresar un número válido.")

        except Exception as e:  # Excepcion general
            print(f"Ocurrió un error inesperado: {e}")



#entrada
opciones=Entry(ventana)
opciones.pack()
opciones.place(relx=0.25, rely=0.7, relwidth=0.49, relheight=0.05)

# Crear botones
btn1 = CTkButton(ventana, font=("sans serif", 13), border_color=c_negro, fg_color=c_azulOscuro,
                 hover_color=c_morado, corner_radius=12, border_width=2, text="Aceptar", height=40,
                 )
btn1.pack()
btn1.place(relx=0.25, rely=0.8, relwidth=0.12, relheight=0.05)

btn2 = CTkButton(ventana, font=("sans serif", 13), border_color=c_negro, fg_color=c_azulOscuro,
                 hover_color=c_morado, corner_radius=12, border_width=2, text="Regresar a Menú", height=40,
                 )
btn2.pack()
btn2.place(relx=0.62, rely=0.8, relwidth=0.12, relheight=0.05)
ventana.mainloop()
