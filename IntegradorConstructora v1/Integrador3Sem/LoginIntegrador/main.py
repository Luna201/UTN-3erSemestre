import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import LoginIntegrador.Menu.menu_principal as menup
from LoginIntegrador.Login.login_comprobacion import validar_ingresos
from LoginIntegrador.Login.registro_usuarios import RegistroUsuario  # Importa la clase RegistroUsuario


class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Constructora BYTEBUSTERS | Iniciar Sesión")

        # Frame
        self.frame = tk.Frame(root)
        self.frame.pack(fill='both', expand=True)

        # Carga y coloca la imagen
        self.cargar_imagen("Image/bytebusters_constructora.png")

        # Frame para el formulario
        self.form_frame = tk.Frame(self.frame)
        self.form_frame.grid(row=0, column=1, padx=20, pady=20)

        # Label Título
        label = tk.Label(self.form_frame, text="Ingreso de usuarios | CONSTRUCTORA BYTEBUSTERS")
        label.grid()

        # Separador horizontal
        self.separador(1, 0, self.form_frame)

        # Guardo los nombres que tendrán los Labels y los posiciono
        campos = ['Usuario', 'Contraseña']
        self.entries = {}  # Diccionario para guardar las respuestas
        for i, campo in enumerate(campos):
            label = tk.Label(self.form_frame, text=campo)
            label.grid(row=2 * i + 2, column=0)
            entry = tk.Entry(self.form_frame, width=30, show="*" if campo == "Contraseña" else "")
            entry.grid(row=2 * i + 3, column=0)
            self.entries[campo] = entry

        # Separador después de los campos
        self.separador(2 * len(campos) + 2, 0, self.form_frame)

        # Label para mensajes de error
        self.error_label = tk.Label(self.form_frame, text="", fg="red")
        self.error_label.grid(row=2 * len(campos) + 4, column=0, pady=10)

        # Frame para los botones
        self.button_frame = tk.Frame(self.form_frame)
        self.button_frame.grid(row=2 * len(campos) + 5, column=0, pady=10)

        # Botón CONFIRMAR
        button = tk.Button(self.button_frame, text="CONFIRMAR", command=self.validar_campos)
        button.grid(row=0, column=0, padx=5)

        # Botón REGISTRARSE
        button_registrar = tk.Button(self.button_frame, text="REGISTRARSE", command=self.ir_a_registrar)
        button_registrar.grid(row=0, column=1, padx=5)

        # Botón CANCELAR
        button_cancelar = tk.Button(self.button_frame, text="CANCELAR", command=self.root.quit)
        button_cancelar.grid(row=0, column=2, padx=5)

    def cargar_imagen(self, ruta_imagen):
        try:
            imagen = Image.open(ruta_imagen)
            imagen = imagen.resize((200, 200), Image.Resampling.LANCZOS)  # Ajusta el tamaño de la imagen
            self.imagen_tk = ImageTk.PhotoImage(imagen)
            self.label_imagen = tk.Label(self.frame, image=self.imagen_tk)
            self.label_imagen.grid(row=0, column=0, padx=10, pady=10)
            self.label_imagen.image = self.imagen_tk  # Mantener una referencia
        except Exception as e:
            print(f"Error al cargar la imagen: {e}")

    def separador(self, fila, columna, frame):
        separador = ttk.Separator(frame, orient='horizontal')
        separador.grid(row=fila, column=columna, columnspan=3, sticky='ew', pady=20)

    def ir_a_registrar(self):
        # Función para abrir la ventana de registro
        self.root.withdraw()  # Oculta la ventana actual
        registrar_root = tk.Tk()  # Crea una nueva ventana para el registro
        registrar_usuario = RegistroUsuario(registrar_root, self.root)  # Pasa la ventana de login a RegistroUsuario
        registrar_root.mainloop()

    def validar_campos(self):
        usuario = self.entries['Usuario'].get()  # Obtenemos los valores usuario y contraseña
        contraseña = self.entries['Contraseña'].get()

        if usuario and contraseña:
            valido, mensaje = validar_ingresos(usuario, contraseña) #--------------------DESCOMENTAR---------------
            self.error_label.config(text=mensaje, fg="green" if valido else "red") #--------------------DESCOMENTAR-------------------
            if valido:
                self.root.destroy()
                menup.llamar_menu_principal()
        else:
            self.error_label.config(text="Por favor, llene todos los campos.")

    def limpiar_campos(self):
        for entry in self.entries.values():
            entry.delete(0, 'end')

    def llamar_login(self):
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    login = Login(root)
    root.mainloop()
