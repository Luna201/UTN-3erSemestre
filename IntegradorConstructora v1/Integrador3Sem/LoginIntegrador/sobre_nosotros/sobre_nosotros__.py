import tkinter as tk
from tkinter import ttk
import LoginIntegrador.Menu.menu_principal as menup

def sobreNosotros():
    # Crear la ventana principal
    root = tk.Tk()
    root.title("Constructora BYTEBUSTERS | Sobre Nosotros")
    root.geometry("860x400+10+10") #Tamaño y posición de la ventana


    # Crear un estilo personalizado
    style = ttk.Style()
    style.configure('TLabel', font=('Helvetica', 16))  # Cambiar tipografía y tamaño de letra

    # Crear un marco para organizar los widgets
    frame = ttk.Frame(root, padding="10")
    frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))


    # primera línea separadora
    separator1 = ttk.Separator(frame, orient='horizontal')
    separator1.grid(row=0, column=0, sticky=(tk.W, tk.E), pady=(5, 5))

    # Título SOBRE NOSOTROS
    label = ttk.Label(frame, text="SOBRE NOSOTROS", style='TLabel',foreground="blue")
    label.grid(row=1, column=0, pady=(5, 5))


    #texto de SOBRE NOSOTROS
    label1 = ttk.Label(frame, text="Byte Busters es una empresa dedicada a la construcción de viviendas con más de 20 años de experiencia.")
    label1.grid(row=2, column=0, pady=(5, 5))
    label1.configure(font=('Helvetica', 12))
    label1 = ttk.Label(frame, text="Nuestro compromiso es ayudarte a hacer realidad el sueño de tener tu casa propia.")
    label1.grid(row=3, column=0, pady=(5, 5))
    label1.configure(font=('Helvetica', 12))
    label1 = ttk.Label(frame, text="Nos destacamos por ofrecer financiación en cuotas fijas en pesos, ajustadas a tu presupuesto.")
    label1.grid(row=4, column=0, pady=(5, 5))
    label1.configure(font=('Helvetica', 12))
    label1 = ttk.Label(frame, text="Contamos con proyectos de construcción en diferentes plazos y una variedad de tipologías de viviendas.")
    label1.grid(row=5, column=0, pady=(5, 5))
    label1.configure(font=('Helvetica', 12))
    label1 = ttk.Label(frame, text="Trabajamos con materiales tradicionales de alta calidad y ofrecemos el sistema llave en mano.")
    label1.grid(row=6, column=0, pady=(5, 5))
    label1.configure(font=('Helvetica', 12))
    label1 = ttk.Label(frame, text="Además, nos encargamos de las instalaciones de servicios, y si no tienes un terreno, te ayudamos a conseguirlo.")
    label1.grid(row=7, column=0, pady=(5, 5))
    label1.configure(font=('Helvetica', 12))


    # ultima línea separadora
    separator1 = ttk.Separator(frame, orient='horizontal')
    separator1.grid(row=8, column=0, sticky=(tk.W, tk.E), pady=(5, 5))

    def ir_a_menu_principal():
        root.destroy()
        menup.llamar_menu_principal()
          # Cerrar la ventana de inicio después de abrir el menú principal


    # Botón para ir al menú principal
    boton_menu = ttk.Button(frame, text="Ir al Menú Principal", command=ir_a_menu_principal)
    boton_menu.grid(row=9, column=0, pady=(10, 20))


    # Ejecutar la aplicación
    root.mainloop()

def llamar_Nosotros():
    sobreNosotros()
    
if __name__ == "__main__":
    llamar_Nosotros() # Llamar esta función