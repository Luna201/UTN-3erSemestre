import tkinter
import tkinter as tk
from customtkinter import CTkButton, CTkLabel, CTkFrame
import chatbot,  nosotros, mod_conceptos, mod_excesos

c_negro = "#010101"
c_morado = "#7f5af0"
c_verde = "#2cb67d"
c_azul = "#33DDFF"
c_azulOscuro = "#2980B9"
c_blanco = "#FFFFFF"
c_azulClaro = "#86A9FD"

def ir_usuario():
    ventana.withdraw()
    nosotros.ir_nosotros()
def ir_balance():
    ventana.withdraw()
    chatbot.ir_chatbot()
def ir_conceptos():
    ventana.withdraw()
    mod_conceptos.ir_conceptos()

def ir_excesos():
    ventana.withdraw()
    mod_excesos.ir_excesos()

def ir_menu():
    global ventana
    ventana = tkinter.Tk()
    ancho_pantalla = ventana.winfo_screenwidth()
    altura_pantalla = ventana.winfo_screenheight()
    ancho_ventana = int(ancho_pantalla)
    altura_ventana = int(altura_pantalla)
    ventana.geometry(f"{ancho_ventana}x{altura_ventana}")
    ventana.config(bg=c_azulClaro)
    ventana.title("Byte Busters Travel")

    label_inicio = tk.Label(ventana, text="#     Bienvenido     #", bd=2, bg=c_azulClaro, fg="black", font=("Verdana", 18))
    label_inicio.pack(pady=20)

    # Crear botones
    btn1 = CTkButton(ventana, font=("sans serif", 13), border_color=c_negro, fg_color=c_azulOscuro,
                     hover_color=c_morado, corner_radius=12, border_width=2, text="Nosotros", height=40,
                     command=nosotros.ir_nosotros)
    btn1.pack()
    btn1.place(relx=0.25, rely=0.2, relwidth=0.12, relheight=0.05)

    btn2 = CTkButton(ventana, font=("sans serif", 13), border_color=c_negro, fg_color=c_azulOscuro,
                     hover_color=c_morado, corner_radius=12, border_width=2, text="Chatbot", height=40,
                     command=chatbot.ir_chatbot)
    btn2.pack()
    btn2.place(relx=0.25, rely=0.3, relwidth=0.12, relheight=0.05)


    btn5 = CTkButton(ventana, font=("sans serif", 13), border_color=c_negro, fg_color=c_azulOscuro,
                     hover_color=c_morado, corner_radius=12, border_width=2, text="3",
                     height=40,
                     command=ir_conceptos)
    btn5.pack()
    btn5.place(relx=0.62, rely=0.2, relwidth=0.12, relheight=0.05)

    btn6 = CTkButton(ventana, font=("sans serif", 13), border_color=c_negro, fg_color=c_azulOscuro,
                     hover_color=c_morado, corner_radius=12, border_width=2, text="4", height=40,
                     command=ir_excesos)
    btn6.pack()
    btn6.place(relx=0.62, rely=0.3, relwidth=0.12, relheight=0.05)


    btn9 = CTkButton(ventana, font=("sans serif", 13), border_color=c_negro, fg_color=c_azulOscuro,
                     hover_color=c_morado, corner_radius=12, border_width=2, text="Salir", height=40,
                     command=ventana.quit)
    btn9.pack()
    btn9.place(relx=0.44, rely=0.7, relwidth=0.12, relheight=0.05)

    ventana.mainloop()
