from tkinter import messagebox
import tkinter as tk
from customtkinter import CTkButton

# Colores
c_azulClaro = "#86A9FD"
c_negro = "#010101"
c_morado = "#7f5af0"
c_verde = "#2cb67d"
c_azul = "#33DDFF"
c_azulOscuro = "#2980B9"

# Variables globales
step = 1
tema = 0
m2 = 0
costo = 0
linea = 0
adelanto = 0
restoApagar = 0
pagoFinal = 0
cuotas = 0


def ir_chatbot(ventana_anterior):
    global step, tema, m2, costo, linea, adelanto, restoApagar, pagoFinal, cuotas

    def show_step():
        text_box.config(state=tk.NORMAL)
        text_box.delete('1.0', tk.END)

        if step == 1:
            text_box.insert(tk.END, """
            __ Bienvenido a chatbot de Byte Busters Travels __
Seleccione el tema a consultar:
 (1) Grupos\n (2) Fechas\n (3) Lugar de partidos\n (4) Planes de pago\n """)

        elif step == 2:
            if tema == 1:
                text_box.insert(tk.END, """
            ---     Formación de grupos     ---
 (1) Grupo A: Argentina - Perú - Chile - Canada\n (2) Grupo B: México - Ecuador - Venezuela - Jamaica
 (3) Grupo C: Estados Unidos - Uruguay - Panamá - Bolivia\n (4) Grupo D: Brasil - Colombia - Costa Rica - Paraguay\n""")
            elif tema == 2:
                text_box.insert(tk.END, """
            ---     ¿Que fecha quiere consultar?     ---
 (1) Fecha 1: Argentina vs Canada / Peru vs Chile / México vs Jamaica / Ecuador vs Venezuela /
                         EE.UU vs Bolivia / Uruguay vs Panamá / Brasil vs Costa Rica / Colombia vs Paraguay
 (2) Fecha 2: Argentina vs Chile / Peru vs Canada / México vs Venezuela / Ecuador vs Jamaica /
                         EE.UU vs Panamá / Uruguay vs Bolivia / Brasil vs Paraguay / Colombia vs Costa Rica
 (3) Fecha 3:Argentina vs Peru / Canada vs Chile / México vs Ecuador / Jamaica vs Venezuela /
                         EE.UU vs Uruguay / Bolivia vs Panamá / Brasil vs Colombia / Costa Rica vs Paraguay
 (4) Cuartos de Final: 1B vs 2A / 1A vs 2B / 1D vs 2C / 1C vs 2D
 (5) Semifinal: Ganador (1B vs 2A) vs Ganador (1A vs 2B) / Ganador (1D vs 2C) vs Ganador (1C vs 2D)
 (6) Final:  Final y 3er Puesto""")
            elif tema == 3:
                text_box.insert(tk.END, """
                       __ Seleccione el tamaño de m2: __
        (1) 80 m2\n (2) 100 m2\n (3) 120 m2\n (4) Volver a Cotización\n """)

        elif step == 3:
            text_box.insert(tk.END, """
                   __ Seleccione la línea que desea: __
        (1) Estándar ($ 299.000 el m2)\n (2) Premium ($ 348.000 el m2)\n (3) Country ($ 420.000 el m2)\n (4) Volver a Cotización\n """)
        elif step == 6:
            text_box.insert(tk.END, """
                   -- ¿Qué desea hacer? --
        (1) Realizar otra cotización\n (2) Salir al menú principal\n """)

        text_box.config(state=tk.DISABLED)

    def next_step():
        global step, tema, m2, costo, linea, adelanto, restoApagar, pagoFinal, cuotas
        try:
            if step == 1:
                tema = int(entry.get())
                if tema not in [1, 2, 3, 4]:
                    raise ValueError
            elif step == 2:
                if tema == 1:
                    grupo = int(entry.get())
                    if grupo not in [1, 2, 3, 4]:
                        raise ValueError
                elif tema == 2:
                    m2 = int(entry.get())
                    if m2 not in [1, 2, 3, 4]:
                        raise ValueError
                elif tema == 3:
                    m2 = int(entry.get())
                    if m2 not in [1, 2, 3, 4]:
                        raise ValueError
            elif step == 3:
                linea = int(entry.get())
                if linea not in [1, 2, 3, 4]:
                    raise ValueError

            step += 1
            show_step()
            entry.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Error", "Elige una opción válida.")

    def back_step():
        global step
        if step > 1:
            step -= 1
            show_step()
            entry.delete(0, tk.END)
        else:
            reiniciar()

    def reiniciar():
        global step, tema, m2, costo, linea, adelanto, restoApagar, pagoFinal, cuotas
        step = 1
        tema = 0
        m2 = 0
        costo = 0
        linea = 0
        adelanto = 0
        restoApagar = 0
        pagoFinal = 0
        cuotas = 0
        show_step()
        entry.delete(0, tk.END)

    def volver_al_menu():
        root.destroy()
        ventana_anterior.deiconify()

    root = tk.Tk()
    root.title("Cotización de Construcción")
    ventana_anterior.withdraw()

    text_box = tk.Text(root, wrap=tk.WORD, state=tk.DISABLED, height=10, width=100)
    text_box.pack(pady=20)

    entry = tk.Entry(root)
    entry.pack()
    entry.place(relx=0.44, rely=0.3, relwidth=0.12, relheight=0.05)

    frame = tk.Frame(root)
    frame.pack(pady=20)

    ancho_root = root.winfo_screenwidth()
    altura_root = root.winfo_screenheight()
    ancho_root = int(ancho_root)
    altura_root = int(altura_root)
    root.geometry(f"{ancho_root}x{altura_root}")
    root.config(bg=c_azulClaro)
    root.title("Byte Busters Travel")

    btn_accept = CTkButton(root, font=("sans serif", 13), border_color=c_negro, fg_color=c_azulOscuro,
                           hover_color=c_morado, corner_radius=12, border_width=2, text="Aceptar", height=40,
                           command=next_step)
    btn_accept.pack()
    btn_accept.place(relx=0.3, rely=0.5, relwidth=0.12, relheight=0.05)

    btn_back = CTkButton(root, font=("sans serif", 13), border_color=c_negro, fg_color=c_azulOscuro,
                         hover_color=c_morado, corner_radius=12, border_width=2, text="Regresar", height=40,
                         command=back_step)
    btn_back.pack()
    btn_back.place(relx=0.44, rely=0.5, relwidth=0.12, relheight=0.05)

    boton_menu = CTkButton(root, font=("sans serif", 13), border_color=c_negro, fg_color=c_azulOscuro,
                           hover_color=c_morado, corner_radius=12, border_width=2, text="Ir al Menú Principal",
                           height=40,
                           command=volver_al_menu)
    boton_menu.pack()
    boton_menu.place(relx=0.58, rely=0.5, relwidth=0.12, relheight=0.05)

    btn0 = CTkButton(root, font=("sans serif", 13), border_color=c_negro, fg_color=c_azulOscuro,
                     hover_color=c_morado, corner_radius=12, border_width=2, text="Salir", height=40,
                     command=root.quit)
    btn0.pack()
    btn0.place(relx=0.44, rely=0.7, relwidth=0.12, relheight=0.05)

    show_step()
    root.mainloop()


# Llamada de prueba
ventana_anterior = tk.Tk()  # Crear una ventana de ejemplo para llamar a ir_chatbot
ventana_anterior.withdraw()  # Ocultar la ventana anterior
ir_chatbot(ventana_anterior)
