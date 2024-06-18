import tkinter
import tkinter as tk
from customtkinter import CTkButton, CTkEntry

c_negro = "#010101"
c_morado = "#7f5af0"
c_verde = "#2cb67d"
c_azul = "#33DDFF"
c_azulOscuro = "#2980B9"
c_blanco = "#FFFFFF"
c_azulClaro = "#86A9FD"

"""
def Regrasar():
    ventana.withdraw()
    menu.ir_menu()
"""

def ir_ventana():
    global ventana
    ventana = tkinter.Tk()
    ancho_pantalla = ventana.winfo_screenwidth()
    altura_pantalla = ventana.winfo_screenheight()
    ancho_ventana = int(ancho_pantalla)
    altura_ventana = int(altura_pantalla)
    ventana.geometry(f"{ancho_ventana}x{altura_ventana}")
    ventana.config(bg=c_azulClaro)
    ventana.title("Sistema de cotización")

    label_inicio = tk.Label(ventana, text="   Inicio   ", bd=2, bg=c_azulClaro,
                            fg="black", font=("Verdana", 18))
    label_inicio.pack(pady=20)
    correo = CTkEntry(ventana, font=('sans rerif', 12), placeholder_text='.',
                      border_color=c_azulOscuro, fg_color=c_blanco, width=220, height=40)
    correo.place(x=150, y=145)

    ingreso = CTkEntry(ventana, font=('sans rerif', 12), placeholder_text='Introduzca opcion elegida',
                          border_color=c_azulOscuro, fg_color=c_blanco, width=220, height=40)
    ingreso.place(x=150, y=200)

    volver = CTkButton(ventana, font=("sans serif", 12), border_color=c_negro, fg_color=c_azulOscuro,
                           hover_color=c_verde, corner_radius=12, border_width=2, text="volver", height=40)
    volver.place(x=180, y=400)

    ventana.mainloop()