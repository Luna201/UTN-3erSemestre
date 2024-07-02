import tkinter as tk
from tkinter import messagebox

import LoginIntegrador.Menu.menu_principal as menup



# Inicialización de variables globales
step = 1
tamanio = 0
m2 = 0
costo = 0
linea = 0
adelanto = 0
restoApagar = 0
pagoFinal = 0
cuotas = 0

def ir_cotizacion():
    global step, tamanio, m2, costo, linea, adelanto, restoApagar, pagoFinal, cuotas

    def show_step():
        # Ocultar widgets de adelanto si están visibles
        adelanto_input.pack_forget()
        adelanto_button.pack_forget()
        entry.pack()
        label.pack()

        # Mostrar el mensaje correspondiente a cada paso
        if step == 1:
            text.set("""
            __ Bienvenido a la sección de Cotización __
Seleccione el tamaño de la construcción:
 (1) Pequeño\n (2) Mediano\n (3) Grande\n (4) Volver a MENÚ\n """)
        elif step == 2:
            if tamanio == 1:
                text.set("""
                __ Seleccione el tamaño de m2: __
 (1) 45 m2\n (2) 60 m2\n (3) 75 m2\n (4) Volver a Cotización\n """)
            elif tamanio == 2:
                text.set("""
                __ Seleccione el tamaño de m2: __
 (1) 70 m2\n (2) 90 m2\n (3) 105 m2\n (4) Volver a Cotización\n """)
            elif tamanio == 3:
                text.set("""
                __ Seleccione el tamaño de m2: __
 (1) 80 m2\n (2) 100 m2\n (3) 120 m2\n (4) Volver a Cotización\n """)
        elif step == 3:
            text.set("""
            __ Seleccione la línea que desea: __
 (1) Estándar ($ 299.000 el m2)\n (2) Premium ($ 348.000 el m2)\n (3) Country ($ 420.000 el m2)\n (4) Volver a Cotización\n """)
        elif step == 4:
            text.set("""
            -- Digite una opción de menú: --
 (1) SI ingresar adelanto\n (2) NO ingresar adelanto\n (3) Volver a Cotización\n """)
        elif step == 5:
            text.set("""
            --¿En cuantas cuotas desea pagar?: --
 (1) 12 cuotas (0% interes)\n (2) 24 cuotas (interes: 50%)\n (3) 36 cuotas (interes: 75%)\n (4) Volver a Cotización\n """)
        elif step == 6:
            text.set("""
            -- ¿Qué desea hacer? --
 (1) Realizar otra cotización\n (2) Salir al menú principal\n """)

    def next_step():
        global step, tamanio, m2, linea, costo, adelanto, restoApagar, pagoFinal, cuotas
        try:
            if step == 1:
                tamanio = int(entry.get())
                if tamanio not in [1, 2, 3, 4]:
                    raise ValueError
                if tamanio == 4:
                    reiniciar()
                    return
            elif step == 2:
                m2 = int(entry.get())
                if m2 not in [1, 2, 3, 4]:
                    raise ValueError
                if m2 == 4:
                    step = 1
            elif step == 3:
                linea = int(entry.get())
                if linea not in [1, 2, 3, 4]:
                    raise ValueError
                if linea == 4:
                    step = 2
                    show_step()
                    return

                # Calcular el costo basado en el tamaño y la línea seleccionada
                if tamanio == 1:
                    if m2 == 1:
                        costo = 45 * (299000 if linea == 1 else 348000 if linea == 2 else 420000)
                    elif m2 == 2:
                        costo = 60 * (299000 if linea == 1 else 348000 if linea == 2 else 420000)
                    elif m2 == 3:
                        costo = 75 * (299000 if linea == 1 else 348000 if linea == 2 else 420000)
                elif tamanio == 2:
                    if m2 == 1:
                        costo = 70 * (299000 if linea == 1 else 348000 if linea == 2 else 420000)
                    elif m2 == 2:
                        costo = 90 * (299000 if linea == 1 else 348000 if linea == 2 else 420000)
                    elif m2 == 3:
                        costo = 105 * (299000 if linea == 1 else 348000 if linea == 2 else 420000)
                elif tamanio == 3:
                    if m2 == 1:
                        costo = 80 * (299000 if linea == 1 else 348000 if linea == 2 else 420000)
                    elif m2 == 2:
                        costo = 100 * (299000 if linea == 1 else 348000 if linea == 2 else 420000)
                    elif m2 == 3:
                        costo = 120 * (299000 if linea == 1 else 348000 if linea == 2 else 420000)

                messagebox.showinfo("Cotización", f"El costo es: $ {costo}")

            elif step == 4:
                opcionAdelanto = int(entry.get())
                if opcionAdelanto not in [1, 2, 3]:
                    raise ValueError
                if opcionAdelanto == 1:
                    text.set("¿Cuánto dinero desea ingresar?")
                    entry.pack_forget()
                    adelanto_input.pack()
                    adelanto_button.pack()
                    return
                elif opcionAdelanto == 2:
                    adelanto = 0
                elif opcionAdelanto == 3:
                    step = 3
                    show_step()
                    return
                restoApagar = costo - adelanto
                messagebox.showinfo("Adelanto", f"El adelanto es: $ {adelanto}\nResto a pagar: $ {restoApagar}")

            elif step == 5:
                tiempoPago = int(entry.get())
                if tiempoPago not in [1, 2, 3, 4]:
                    raise ValueError
                if tiempoPago == 1:
                    pagoFinal = restoApagar
                    cuotas = pagoFinal / 12
                elif tiempoPago == 2:
                    pagoFinal = (restoApagar * 150) / 100
                    cuotas = pagoFinal / 24
                elif tiempoPago == 3:
                    pagoFinal = (restoApagar * 175) / 100
                    cuotas = pagoFinal / 36
                elif tiempoPago == 4:
                    step = 4
                    show_step()
                    return

                messagebox.showinfo("Cuotas", f"""
                --ELECCIONES REALIZADAS:
 # TAMAÑO DE CONSTRUCCIÓN: {tamanio}\n # DIMENSIÓN EN m2: {m2}\n # LINEA DE CONSTRUCCIÓN: {linea}\n # IMPORTE BRUTO: ${costo}
 # ADELANTO ENTREGADO: $ {adelanto}\n # COSTO TOTAL FINAL: ${pagoFinal}, EN CUOTAS DE: ${cuotas} MENSUALES""")

            elif step == 6:
                siguiente_paso = int(entry.get())
                if siguiente_paso == 1:
                    reiniciar()
                    return
                elif siguiente_paso == 2:
                    root.destroy()
                    menup.llamar_menu_principal()

                    return

            step += 1
            show_step()
            entry.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Error", "Elige una opción válida.")

    def enter_adelanto():
        global adelanto, restoApagar, step
        try:
            adelanto = float(adelanto_input.get())
            restoApagar = costo - adelanto
            messagebox.showinfo("Adelanto", f"El adelanto es: $ {adelanto}\nResto a pagar: $ {restoApagar}")
            adelanto_input.pack_forget()
            adelanto_button.pack_forget()
            entry.pack()
            label.pack()
            step += 1
            show_step()
        except ValueError:
            messagebox.showerror("Error", "Ingrese un valor válido.")

    def back_step():
        global step
        if step > 1:
            step -= 1
            show_step()
            entry.delete(0, tk.END)
        else:
            reiniciar()

    def reiniciar():
        global step, tamanio, m2, costo, linea, adelanto, restoApagar, pagoFinal, cuotas
        step = 1
        tamanio = 0
        m2 = 0
        costo = 0
        linea = 0
        adelanto = 0
        restoApagar = 0
        pagoFinal = 0
        cuotas = 0
        show_step()
        entry.delete(0, tk.END)

    # Crear la ventana principal
    root = tk.Tk()
    root.title("Cotización de Construcción")

    # Crear y configurar widgets
    text = tk.StringVar()
    label = tk.Label(root, textvariable=text, wraplength=400)
    label.pack(pady=20)

    entry = tk.Entry(root)
    entry.pack(pady=10)

    frame = tk.Frame(root)
    frame.pack(pady=20)

    #tamaño Ventana
    ancho_ventana = 900
    alto_ventana = 300

    x_ventana = root.winfo_screenwidth() // 2 - ancho_ventana // 2
    y_ventana = root.winfo_screenheight() // 2 - alto_ventana // 2

    posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
    root.geometry(posicion)

    root.resizable(0, 0)

    #Botones
    btn_accept = tk.Button(frame, text="Aceptar", command=next_step)
    btn_accept.pack(side=tk.LEFT, padx=5)

    btn_back = tk.Button(frame, text="Regresar", command=back_step)
    btn_back.pack(side=tk.LEFT, padx=5)

    def ir_a_menu_principal():
        root.destroy()
        menup.llamar_menu_principal()
          # Cerrar la ventana de inicio después de abrir el menú principal


    # Botón para ir al menú principal
    boton_menu = tk.Button(frame, text="Ir al Menú Principal", command=ir_a_menu_principal)
    boton_menu.pack(side=tk.LEFT, padx=5)

    adelanto_input = tk.Entry(root)
    adelanto_button = tk.Button(root, text="Ingresar Adelanto", command=enter_adelanto)

    show_step()

    root.mainloop()



