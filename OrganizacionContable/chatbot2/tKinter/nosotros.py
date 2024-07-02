import tkinter as tk
from customtkinter import CTkButton

c_azulClaro = "#86A9FD"
c_negro = "#010101"
c_morado = "#7f5af0"
c_verde = "#2cb67d"
c_azul = "#33DDFF"
c_azulOscuro = "#2980B9"

def ir_nosotros():

    def volver_al_menu():
        root.destroy()

    root = tk.Tk()
    root.title("Cotización de Construcción")

    ancho_root = root.winfo_screenwidth()
    altura_root = root.winfo_screenheight()
    ancho_root = int(ancho_root)
    altura_root = int(altura_root)
    root.geometry(f"{ancho_root}x{altura_root}")
    root.config(bg=c_azulClaro)
    root.title("Byte Busters Travel")


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

    root.mainloop()