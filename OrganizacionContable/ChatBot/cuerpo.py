import tkinter as tk
from customtkinter import CTkButton

c_negro = "#010101"
c_morado = "#7f5af0"
c_verde = "#2cb67d"
c_azul = "#33DDFF"
c_azulOscuro = "#2980B9"
c_blanco = "#FFFFFF"
c_azulClaro = "#86A9FD"

def responder_preguntas():
    pregunta1 = entry_pregunta1.get()

    # Aquí procesas las preguntas y generas las respuestas con Gemini
    # Por ahora, solo imprimimos las preguntas en la consola y mostramos respuestas falsas
    print("Pregunta 1:", pregunta1)

    # Ejemplo de respuestas falsas
    respuesta1 = "Respuesta a la pregunta 1"
    text_respuestas.config(state=tk.NORMAL)
    text_respuestas.insert(tk.END, "Gemini dice:\n")
    text_respuestas.insert(tk.END, "Pregunta 1: " + respuesta1 + "\n")
    text_respuestas.config(state=tk.DISABLED)

def ir_chat():
    global ventana
    ventana = tk.Tk()
    ventana.geometry("700x800")  # Ancho x Alto
    ventana.resizable(False, False)
    ventana.config(bg=c_azulClaro)
    ventana.title("ChatBot")

    label_inicio = tk.Label(ventana, text="---   Respuestas Ya   ---", bd=2, bg=c_azulClaro, fg="black", font=("Verdana", 18))
    label_inicio.pack(pady=20)

    # Cuadro de texto para la primera pregunta
    global entry_pregunta1
    entry_pregunta1 = tk.Entry(ventana, font=("Verdana", 12))
    entry_pregunta1.pack(pady=10)
    entry_pregunta1.place(x=20, y=15)

    # Botón para enviar las preguntas
    btn_enviar = CTkButton(ventana, font=("sans serif", 13), border_color=c_negro, fg_color=c_azulOscuro,
                     hover_color=c_morado, corner_radius=12, border_width=2, text="Enviar Preguntas", height=40,
                     command=responder_preguntas)
    btn_enviar.pack()
    btn_enviar.place(relx=0.8, rely=0.5, relwidth=0.2, relheight=0.4)

    # Área de texto para las respuestas
    global text_respuestas
    text_respuestas = tk.Text(ventana, font=("Verdana", 12), bg="white", wrap=tk.WORD)
    text_respuestas.pack(pady=50, padx=50, fill=tk.BOTH, expand=True)
    text_respuestas.config(state=tk.DISABLED)

    ventana.mainloop()

ir_chat()
