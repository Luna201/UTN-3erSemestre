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
grupos = 0
fechas = 0
lugar = 0

def ir_chatbot(ventana_anterior):
    global step, tema, grupos, fechas, lugar, cuotas

    def show_step():
        text_box.config(state=tk.NORMAL)
        text_box.delete('1.0', tk.END)

        if step == 1:
            text_box.insert(tk.END, """
                __ Bienvenido a la sección de Cotización __
Seleccione el tamaño de la construcción:
 (1) Grupos\n (2) Fechas\n (3) Lugar de partidos\n """)

        elif step == 2:
            if tema == 1:
                text_box.insert(tk.END, """
            ---     Formación de grupos     ---
 Grupo A: Argentina - Perú - Chile - Canada\n Grupo B: México - Ecuador - Venezuela - Jamaica
 Grupo C: Estados Unidos - Uruguay - Panamá - Bolivia\n Grupo D: Brasil - Colombia - Costa Rica - Paraguay
 
 Presione 0 para Volver\n""")
            elif tema == 2:
                text_box.insert(tk.END, """
            ---     ¿Qué fecha quiere consultar?     ---
 Fecha 1: Argentina vs Canada / Peru vs Chile / México vs Jamaica / Ecuador vs Venezuela /
          EE.UU vs Bolivia / Uruguay vs Panamá / Brasil vs Costa Rica / Colombia vs Paraguay
 Fecha 2: Argentina vs Chile / Peru vs Canada / México vs Venezuela / Ecuador vs Jamaica /
          EE.UU vs Panamá / Uruguay vs Bolivia / Brasil vs Paraguay / Colombia vs Costa Rica
 Fecha 3: Argentina vs Peru / Canada vs Chile / México vs Ecuador / Jamaica vs Venezuela /
          EE.UU vs Uruguay / Bolivia vs Panamá / Brasil vs Colombia / Costa Rica vs Paraguay
 Cuartos de Final: 1ro grupo B vs 2do grupo A / 1ro grupo A vs 2do grupo B / 1ro grupo D vs 2do grupo C / 1ro grupo C vs 2do grupo D
 Semifinal: Ganador (1B vs 2A) vs Ganador (1A vs 2B) / Ganador (1D vs 2C) vs Ganador (1C vs 2D)
 Final: Final y 3er Puesto
 
 Presione 0 para Volver""")
            elif tema == 3:
                text_box.insert(tk.END, """
           __ Lugar a jugar: __
 (1) Fase de grupos\n (2) Cuartos de final\n (3) Semifinales\n (4) 3er Puesto y Final\n (0) Volver\n""")

        elif step == 3:
            if lugar == 1:
                text_box.insert(tk.END, """
Costa Este      East Rutherford, NJ: Argentina vs Chile (25/06) // Uruguay vs Bolivia (27/06)
                Miami, FL: Uruguay vs Panama (23/06) // Argentina vs Peru (29/06)
                Orlando, FL: Canada vs Chile (29/06) // Bolivia vs Panama (01/07)
                Atlanta, GA: Argentina vs Canada (20/06) // Panama vs USA (27/06)

Centro          Kansas City, MO: Uruguay vs USA (01/07)
                Kansas City, KS: Peru vs Canada (25/06)
                Arlington, TX: Peru vs Chile (21/06) // Bolivia vs USA (23/06)
                Houston, TX: Mexico vs Jamaica (22/06) // Colombia vs Paraguay (24/06)
                Austin, TX: Venezuela vs Jamaica (30/06) // Costa Rica vs Paraguay (02/07)

Costa Oeste     Glendale, AZ: Colombia vs Costa Rica (24/06) // Mexico vs Ecuador (30/06)
                Las Vegas, NV: Ecuador vs Jamaica (26/06) // Paraguay vs Brasil (24/06)
                Inglewood, CA: Brasil vs Costa Rica (24/06) // Mexico vs Venezuela (26/06)
                Santa Clara, CA: Venezuela vs Ecuador (30/06) // Brasil vs Colombia (02/07)

Presione 0 para Volver""")
            elif lugar == 2:
                text_box.insert(tk.END, """
Centro         Arlington, TX: 1ro grupo B vs 2do grupo A (05/07)  
               Houston, TX: 1ro grupo A vs 2do grupo B (04/07)  

Costa Oeste    Glendale, AZ: 1ro grupo D vs 2do grupo C (06/07) 
               Las Vegas, NV: 1ro grupo C vs 2do grupo D (06/07)

Presione 0 para Volver""")
            elif lugar == 3:
                text_box.insert(tk.END, """
Costa Este     East Rutherford, NJ: Ganador (1B vs 2A) vs Ganador (1A vs 2B) (09/07)
               Charlotte, GA: Ganador (1D vs 2C) vs Ganador (1C vs 2D) (10/07)
               
Presione 0 para Volver""")
            elif lugar == 4:
                text_box.insert(tk.END, """
Costa Este      Charlotte, GA: 3er Lugar (13/07) 
                Miami, FL: FINAL (14/07)

Presione 0 para Volver""")

        text_box.config(state=tk.DISABLED)
        entry.delete(0, tk.END)

    def next_step():
        global step, tema, grupos, fechas, lugar, cuotas
        try:
            if entry.get() == "0":
                back_step()
                return
            if step == 1:
                tema = int(entry.get())
                if tema not in [1, 2, 3]:
                    raise ValueError
            elif step == 2:
                if tema == 1:
                    grupos = int(entry.get())
                    if grupos not in [0]:
                        raise ValueError
                elif tema == 2:
                    fechas = int(entry.get())
                    if fechas not in [0]:
                        raise ValueError
                elif tema == 3:
                    lugar = int(entry.get())
                    if lugar not in [1, 2, 3, 4]:
                        raise ValueError
            elif step == 3:
                if lugar == 1:
                    enter = int(entry.get())
                    if enter not in [0]:
                        raise ValueError
                if lugar == 2:
                    enter = int(entry.get())
                    if enter not in [0]:
                        raise ValueError
                if lugar == 3:
                    enter = int(entry.get())
                    if enter not in [0]:
                        raise ValueError
                if lugar == 4:
                    enter = int(entry.get())
                    if enter not in [0]:
                        raise ValueError

            step += 1
            show_step()
        except ValueError:
            messagebox.showerror("Error", "Elige una opción válida.")

    def back_step():
        global step
        if step > 1:
            step -= 1
            show_step()

    def volver_al_menu():
        root.destroy()
        ventana_anterior.deiconify()

    root = tk.Tk()
    root.title("Cotización de Construcción")
    ventana_anterior.withdraw()

    text_box = tk.Text(root, wrap=tk.WORD, state=tk.DISABLED, height=30, width=150)
    text_box.pack(pady=20)

    entry = tk.Entry(root)
    entry.pack(pady=10)

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
    btn_accept.place(relx=0.3, rely=0.8, relwidth=0.12, relheight=0.05)

    btn_back = CTkButton(root, font=("sans serif", 13), border_color=c_negro, fg_color=c_azulOscuro,
                         hover_color=c_morado, corner_radius=12, border_width=2, text="Regresar", height=40,
                         command=back_step)
    btn_back.pack()
    btn_back.place(relx=0.44, rely=0.8, relwidth=0.12, relheight=0.05)

    boton_menu = CTkButton(root, font=("sans serif", 13), border_color=c_negro, fg_color=c_azulOscuro,
                           hover_color=c_morado, corner_radius=12, border_width=2, text="Ir al Menú Principal",
                           height=40,
                           command=volver_al_menu)
    boton_menu.pack()
    boton_menu.place(relx=0.58, rely=0.8, relwidth=0.12, relheight=0.05)

    btn0 = CTkButton(root, font=("sans serif", 13), border_color=c_negro, fg_color=c_azulOscuro,
                     hover_color=c_morado, corner_radius=12, border_width=2, text="Salir", height=40,
                     command=root.quit)
    btn0.pack()
    btn0.place(relx=0.44, rely=0.9, relwidth=0.12, relheight=0.05)

    show_step()
    root.mainloop()

def iniciar_app():
    root = tk.Tk()
    root.title("Menú Principal")

    ancho_root = root.winfo_screenwidth()
    altura_root = root.winfo_screenheight()
    ancho_root = int(ancho_root)
    altura_root = int(altura_root)
    root.geometry(f"{ancho_root}x{altura_root}")
    root.config(bg=c_azulClaro)

    btn_start = CTkButton(root, font=("sans serif", 13), border_color=c_negro, fg_color=c_azulOscuro,
                          hover_color=c_morado, corner_radius=12, border_width=2, text="Iniciar Cotización", height=40,
                          command=lambda: ir_chatbot(root))
    btn_start.pack(pady=20)

    btn_exit = CTkButton(root, font=("sans serif", 13), border_color=c_negro, fg_color=c_azulOscuro,
                         hover_color=c_morado, corner_radius=12, border_width=2, text="Salir", height=40,
                         command=root.quit)
    btn_exit.pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    iniciar_app()
