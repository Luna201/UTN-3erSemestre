import tkinter
import tkinter as tk
from customtkinter import CTkButton, CTkEntry
import menu

c_negro = "#010101"
c_morado = "#7f5af0"
c_verde = "#2cb67d"
c_azul = "#33DDFF"
c_azulOscuro = "#2980B9"
c_blanco = "#FFFFFF"
c_azulClaro = "#86A9FD"


def Regrasar():
    ventana.withdraw()
    menu.ir_menu()


def ir_login():
    global ventana
    ventana = tkinter.Tk()
    ventana.geometry("500x500")
    ventana.config(bg=c_azulClaro)
    ventana.title("Sistema de control de facturas")

    label_inicio = tk.Label(ventana, text="   Inicio de Sesion   ", bd=2, bg=c_azulClaro,
                            fg="black", font=("Verdana", 18))
    label_inicio.pack(pady=20)
    correo = CTkEntry(ventana, font=('sans rerif', 12), placeholder_text='Correo electrónico',
                      border_color=c_azulOscuro, fg_color=c_blanco, width=220, height=40)
    correo.place(x=150, y=145)

    contraseña = CTkEntry(ventana, font=('sans rerif', 12), placeholder_text='contraseña',
                          border_color=c_azulOscuro, fg_color=c_blanco, width=220, height=40)
    contraseña.place(x=150, y=200)

    bt_iniciar = CTkButton(ventana, font=("sans serif", 12), border_color=c_negro, fg_color=c_azulOscuro,
                           hover_color=c_verde, corner_radius=12, border_width=2, text="INICIAR SESION", height=40,
                           command=Regrasar)
    bt_iniciar.place(x=180, y=400)

    ventana.mainloop()
