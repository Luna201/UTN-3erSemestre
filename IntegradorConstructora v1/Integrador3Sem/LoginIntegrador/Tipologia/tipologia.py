import tkinter as tk
from tkinter import messagebox

import LoginIntegrador.Menu.menu_principal as menup

class Tipologia:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tipología de Viviendas")

        self.opcion = None

        self.menu_principal()

    def menu_principal(self):
        self.clear_window()

        label = tk.Label(self.root, text="TIPOLOGÍA", font=("Helvetica", 16))
        label.pack(pady=10)

        opciones = [
            "1. Small Home",
            "2. Medium Home",
            "3. Big Home",
            "4. Volver al menú principal"
        ]

        for opcion in opciones:
            btn = tk.Button(self.root, text=opcion, command=lambda o=opcion: self.elegir_opcion(o), width=40)
            btn.pack(pady=5, padx=15)

    def elegir_opcion(self, opcion):
        if opcion.startswith("1"):
            self.opcion = 1
            self.small_home()
        elif opcion.startswith("2"):
            self.opcion = 2
            self.medium_home()
        elif opcion.startswith("3"):
            self.opcion = 3
            self.big_home()
        elif opcion.startswith("4"):
            self.root.destroy()
            menup.llamar_menu_principal()


    def small_home(self):
        self.clear_window()

        info = "\n*** SMALL HOME ***\n" \
               "Esta Tipología cuenta con cocina integrada al comedor y sala de estar, dormitorio y baño, generando un nucleo de zona nocturna diferenciada de la zona diurna y de servicio.\n" \
               "\n  PODEMOS OPTAR POR:\n" \
               "* 45m2 1 dormitorio\n" \
               "* 60m2 2 dormitorios\n" \
               "* 74m2 3 dormitorios\n"

        self.mostrar_info("Small Home", info)

    def medium_home(self):
        self.clear_window()

        info = "\n*** MEDIUM HOME ***\n" \
               "Esta Tipología cuenta con cocina integrada al comedor y sala de estar\n" \
               "\n  PODEMOS OPTAR POR:\n" \
               "* 70m2 1 dormitorio\n" \
               "* 88m2 2 dormitorios\n" \
               "* 103m2 3 dormitorios\n"

        self.mostrar_info("Medium Home", info)

    def big_home(self):
        self.clear_window()

        info = "\n*** BIG HOME ***\n" \
               "Esta Tipología cuenta con una cocina integrada al comedor y sala de estar, con la opción de optar por 1, 2 o 3 dormitorios amplios y baño. Baño principal con antebaño y posibilidad de lavandería + toilette.\n" \
               "\n  PODEMOS OPTAR POR:\n" \
               "* 73m2 1 dormitorio\n" \
               "* 92m2 2 dormitorios\n" \
               "* 120m2 3 dormitorios\n"

        self.mostrar_info("Big Home", info)

    def mostrar_info(self, tipo, info):
        label = tk.Label(self.root, text=tipo, font=("Helvetica", 14, "bold"))
        label.pack(pady=10)

        text = tk.Text(self.root, wrap=tk.WORD, width=60, height=10)
        text.pack(pady=10)
        text.insert(tk.END, info)
        text.config(state=tk.DISABLED)

        back_btn = tk.Button(self.root, text="Volver", command=self.menu_principal)
        back_btn.pack(pady=5)

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()


    def start(self):
        self.root.mainloop()