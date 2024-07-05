import tkinter as tk
from tkinter import ttk
import LoginIntegrador.Menu.menu_principal as menup


def inicio_ventana():


# Crearmos la ventana principal
    root = tk.Tk()
    root.title("Constructora BYTEBUSTERS | Inicio")
    root.geometry("860x700+10+10") #Tamaño y posición de la ventana
    label = ttk.Style()
    label.configure('TLabel', font=('Helvetica', 16)) #Tipografía y tamaño de la letra


    # Creamos un marco para organizar los widgets
    frame = ttk.Frame(root, padding="10")
    frame.grid(row=0, column=0)


    # primera línea separadora
    separator1 = ttk.Separator(frame, orient='horizontal')
    separator1.grid(row=0, column=0, sticky=(tk.W, tk.E), pady=(5, 5))

    # Título y sus párrafos con sus respectivos tamaños
    label = ttk.Label(frame, text=" BYTE BUSTERS ", foreground="blue")
    label.grid(row=1, column=0, pady=(5, 5))

    label1 = ttk.Label(frame, text="--- Incrementa las ganas de poder hacer tu sueño realidad ---")
    label1.grid(row=2, column=0, pady=(5, 5))
    label1.configure(font=('Helvetica', 12))

    label1 = ttk.Label(frame, text="Podes acceder a tu PROPIA CASA por medio de una FINANCIACIÓN EN CUOTAS y ACORDE A TU PRESUPUESTO")
    label1.grid(row=3, column=0, pady=(5, 5))
    label1.configure(font=('Helvetica', 12))


    # segunda y tercera línea separadora
    separator2 = ttk.Separator(frame, orient='horizontal')
    separator2.grid(row=4, column=0, sticky=(tk.W, tk.E), pady=(5, 30))

    separator1 = ttk.Separator(frame, orient='horizontal')
    separator1.grid(row=5, column=0, sticky=(tk.W, tk.E), pady=(0, 0))

    #Título secundario -- PROYECTOS
    label3 = ttk.Label(frame, text="---- PROYECTOS ----",foreground="purple")
    label3.grid(row=6, column=0, pady=(1, 1))
    label3.configure(font=('Helvetica', 14))

    #párrafos de PROYECTOS
    label1 = ttk.Label(frame, text="Nuestros Proyectos de construcción cuentan con diferentes líneas constructivas, diseños modernos")
    label1.grid(row=7, column=0, pady=(1, 1))
    label1.configure(font=('Helvetica', 12))

    label1 = ttk.Label(frame, text="y distintas tipologías de 1, 2 y 3 dormitorios que se adaptan a la necesidad de cada familia.")
    label1.grid(row=8, column=0, pady=(1, 25))
    label1.configure(font=('Helvetica', 12))


    #Título secundario -- MATERIAL TRADICIONAL
    label3 = ttk.Label(frame, text="---- MATERIAL TRADICIONAL ----",foreground="purple")
    label3.grid(row=9, column=0, pady=(1,1))
    label3.configure(font=('Helvetica', 14))

    #párrafos de MATERIAL TRADICIONAL
    label1 = ttk.Label(frame, text="Construcción de mampostería, en ladrillo, estructura antisísmica de hormigón elaborado, fundación acorde ")
    label1.grid(row=10, column=0, pady=(1,1))
    label1.configure(font=('Helvetica', 12))
    label1 = ttk.Label(frame, text="al tipo de suelo y techo de loza alivianada con viguetas y losetas o de chapa con machimbre")
    label1.grid(row=11, column=0, pady=(1,25))
    label1.configure(font=('Helvetica', 12))

    #Título secundario -- SISTEMA LLAVE EN MANO
    label3 = ttk.Label(frame, text="---- SISTEMA LLAVE EN MANO ----",foreground="purple")
    label3.grid(row=12, column=0, pady=(1,1))
    label3.configure(font=('Helvetica', 14))

    #párrafos de SISTEMA LLAVE EN MANO
    label1 = ttk.Label(frame, text="Nuestro sistema llave en mano incluye vivienda totalmente terminada, con revoques y pintura exterior, revoques finos y ")
    label1.grid(row=13, column=0, pady=(1,1))
    label1.configure(font=('Helvetica', 12))
    label1 = ttk.Label(frame, text="pintura interior, aberturas de aluminio, baño con revestimiento en piso y pared, griferías y sanitarios,")
    label1.grid(row=14, column=0, pady=(1,1))
    label1.configure(font=('Helvetica', 12))
    label1 = ttk.Label(frame, text="cocina instalada con grifería incluida, mesada y bajo mesada de MDF.")
    label1.grid(row=15, column=0, pady=(1,25))
    label1.configure(font=('Helvetica', 12))

    #Título secundario -- TERRENO
    label3 = ttk.Label(frame, text="---- TERRENO ----",foreground="purple")
    label3.grid(row=16, column=0, pady=(1,1))
    label3.configure(font=('Helvetica', 14))

    #párrafos de TERRENO
    label1 = ttk.Label(frame, text="Construímos tu vivienda en tu lote, y en caso de que no poseas, la empresa te permite junto a tu familia elegir.")
    label1.grid(row=17, column=0, pady=(1,1))
    label1.configure(font=('Helvetica', 12))
    label1 = ttk.Label(frame, text="el lote en el lugar que prefieran y financiarlo junto con tu vivienda.")
    label1.grid(row=18, column=0, pady=(1,25))
    label1.configure(font=('Helvetica', 12))

    #Título secundario -- INSTALACIONES
    label3 = ttk.Label(frame, text="---- INSTALACIONES ----",foreground="purple")
    label3.grid(row=19, column=0, pady=(1,1))
    label3.configure(font=('Helvetica', 14))

    #párrafos de INSTALACIONES
    label1 = ttk.Label(frame, text="Instalación de Servicios, luz, agua, cloacas y gas.")
    label1.grid(row=20, column=0, pady=(1,10))
    label1.configure(font=('Helvetica', 12))


    # cuarta línea separadora
    separator1 = ttk.Separator(frame, orient='horizontal')
    separator1.grid(row=21, column=0, sticky=(tk.W, tk.E), pady=(1, 1))

    def ir_a_menu_principal():
        root.destroy()
        menup.llamar_menu_principal()
          # Cerrar la ventana de inicio después de abrir el menú principal


    # Botón para ir al menú principal
    boton_menu = ttk.Button(frame, text="Ir al Menú Principal", command=ir_a_menu_principal)
    boton_menu.grid(row=22, column=0, pady=(10, 20))


    # Para ejecutar la aplicación
    root.mainloop()


def llamar_inicio():
    inicio_ventana()


if __name__ == "__main__":
    llamar_inicio() # Llamar esta función para iniciarlo en el menú