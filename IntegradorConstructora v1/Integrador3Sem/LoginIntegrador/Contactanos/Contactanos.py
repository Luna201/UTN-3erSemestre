import tkinter as tk
from tkinter import simpledialog
import LoginIntegrador.Menu.menu_principal as menup
def contactanos():
    # Información de contacto predeterminada
    contactos = [
        ["Brian Difilipo", "2604511997", "Briandifilipo@hotmail.com"],
        ["Dalma Ponce", "3834000000", "dalma@hotmail.com"],
        ["Andrés Luna", "26757656", "andres@hotmail.com"],
        ["Nicol Paidican", "26757656", "nicol@hotmail.com"],
        ["Hernan Vega", "26757656", "hv@hotmail.com"],
        ["Emi Grossi", "26757656", "emi@hotmail.com"]
    ]

    def mostrar_contactos():
        ventana_contactos = tk.Toplevel(root)
        ventana_contactos.title("Contactos")
        for contacto in contactos:
            tk.Label(ventana_contactos, text=f"Nombre: {contacto[0]}").pack()
            tk.Label(ventana_contactos, text=f"WhatsApp: {contacto[1]}").pack()
            tk.Label(ventana_contactos, text=f"Email: {contacto[2]}").pack()
            tk.Label(ventana_contactos, text="").pack()

    def dejar_mensaje():
        mensaje = simpledialog.askstring("Dejar mensaje", "Escribe tu mensaje:")
        if mensaje:
            # Aquí puedes guardar el mensaje o procesarlo según tus necesidades
            print(f"Mensaje recibido: {mensaje}")

    def ir_a_menu_principal():
        root.destroy()
        menup.llamar_menu_principal()

    root = tk.Tk()
    root.title("Contáctanos")
    root.geometry("860x700+10+10")

    label = tk.Label(root, text="Información de contacto")
    label.pack()

    button_contactos = tk.Button(root, text="Mostrar contactos", command=mostrar_contactos)
    button_contactos.pack()

    button_mensaje = tk.Button(root, text="Dejar mensaje", command=dejar_mensaje)
    button_mensaje.pack()



    button_menu_principal = tk.Button(root, text="Ir al Menú Principal", command=ir_a_menu_principal)
    button_menu_principal.pack()

    root.mainloop()

if __name__ == "__main__":
    contactanos()
