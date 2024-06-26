import psycopg2
from tkinter import Tk, Frame, Label, Entry, ttk, Button
import bcrypt


def separador(fila, columna, frame):
    separador = ttk.Separator(frame, orient='horizontal')
    separador.grid(row=fila, column=columna, columnspan=3, sticky='ew', pady=20)


class RegistroUsuario:
    def __init__(self, root, login_root):
        self.root = root
        self.login_root = login_root  # Guarda la referencia de la ventana de login
        self.root.title("Constructora BYTEBUSTERS | Registración")

        # Frame
        self.frame = Frame(root)
        self.frame.pack(fill='both', expand=True)

        root.resizable(False, False)

        # Label Título
        label = Label(self.frame, text="Regístrate aquí a CONSTRUCTORA BYTEBUSTERS")
        label.grid()

        # Separador horizontal
        separador(1, 0, self.frame)

        # Guardo los nommbres que tendrán los Labels y los posiciono con un ciclo for
        campos = ['Nombre', 'Apellido', 'Teléfono', 'Email', 'Usuario', 'Contraseña', 'Confirmar Contraseña']
        self.entries = {}  # Creo diccionario para guardar las respuestas
        for i, campo in enumerate(campos):  # Al multiplicar por i + 2 posiciono cada uno a dos espacios(label y entry)
            label = Label(self.frame, text=campo)
            label.grid(row=2 * i + 2, column=0)
            entry = Entry(self.frame, width=30)
            entry.grid(row=2 * i + 3, column=0)
            self.entries[campo] = entry  # Agrego entrada al diccionario

        # Separador después de los campos
        separador(2 * len(campos) + 2, 0, self.frame)

        # Label para mensajes de error
        self.error_label = Label(self.frame, text="", fg="red")
        self.error_label.grid(row=2 * len(campos) + 3, column=0, pady=10)

        # Botón CONFIRMAR
        button = Button(self.frame, text="CONFIRMAR", command=self.validar_campos)
        button.grid(row=2 * len(campos) + 2, column=0, pady=10)

        # Botón VOLVER
        button = Button(self.frame, text="VOLVER", command=self.volver_al_login) # Funcion para volver
        button.grid(row=2 * len(campos) + 4, column=0, pady=10)

    def volver_al_login(self):
        # Función para volver al login
        self.root.withdraw()  # Oculta la ventana actual
        self.login_root.deiconify()  # Muestra la ventana de login nuevamente

    def validar_campos(self):
        try:  # Intento obtener los valores ingresados y los guardo en variables
            nombre = self.entries['Nombre'].get()
            apellido = self.entries['Apellido'].get()
            telefono = self.entries['Teléfono'].get()
            email = self.entries['Email'].get()
            usuario = self.entries['Usuario'].get()
            contraseña = self.entries['Contraseña'].get()
            confirmar_contraseña = self.entries['Confirmar Contraseña'].get()
            #  Comprobación de que los campos poseen contenido
            if nombre and apellido and telefono and email and usuario and contraseña and confirmar_contraseña:
                if contraseña == confirmar_contraseña:  # confirmación de contraseña
                    #  Utilizo un salt (que añade un valor aleatorio en la contraseña ingresada)
                    #  utilizando la cadena de formato utf-8. Dentro de la función bcrypt.hashpw
                    #  que transforma ambos valores en bytes para ser guardados en la base de datos
                    #  desde la variable contraseña_encriptada
                    contraseña_encriptada = bcrypt.hashpw(contraseña.encode('utf-8'), bcrypt.gensalt())
                    self.error_label.config(text="Registrado Correctamente", fg="green")
                    print("Usuario guardado correctamente")

                    try:
                        conexion = psycopg2.connect(user='postgres',
                                                    password='admin',
                                                    host='127.0.0.1',
                                                    port='5432',
                                                    database='integrador_constructora')

                        with conexion:
                            with conexion.cursor() as cursor:
                                sentencia = (
                                    'INSERT INTO usuarios (nombre, apellido, telefono, email, usuario, contrasenia) VALUES ('
                                    '%s, %s, %s, %s, %s, %s)')
                                valores = (
                                nombre, apellido, telefono, email, usuario, contraseña_encriptada.decode('utf-8'))
                                cursor.execute(sentencia, valores)
                                registros_insertados = cursor.rowcount
                                print(f'Los registros insertados son: {registros_insertados}')

                    except Exception as e:
                        self.error_label.config(text=f'Ocurrió un error: {e}')
                        print(f'Ocurrió un error: {e}')

                    finally:
                        if 'conexion' in locals():
                            conexion.close()

                    self.limpiar_campos()
                else:
                    self.error_label.config(text="Las contraseñas no coinciden")
            else:
                self.error_label.config(text="Por favor, llene todos los campos.")
        except KeyError as e:
            self.error_label.config(text=f"Error al obtener el campo: {e}")
            print(f"Error al obtener el campo: {e}")
    def limpiar_campos(self):  # Funcion para limpiar los campos
        # Limpiar todos los campos de entrada
        for entry in self.entries.values():
            entry.delete(0, 'end')


if __name__ == "__main__":  # se instancia para pruebas
    root = Tk()
    registro_usuario = RegistroUsuario(root)

    root.mainloop()  # ciclo de pantalla principal
