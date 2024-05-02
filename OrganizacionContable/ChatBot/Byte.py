# PROYECTO DE CHATBOT: Organización Contable

import google.generativeai as genai
import tkinter as tk
from customtkinter import CTkButton

c_negro = "#010101"
c_morado = "#7f5af0"
c_verde = "#2cb67d"
c_azul = "#33DDFF"
c_azulOscuro = "#2980B9"
c_blanco = "#FFFFFF"
c_azulClaro = "#86A9FD"


def Preguntar():
    # Se configura la llave de acceso a gemini
    genai.configure(api_key="AIzaSyD-p5XxwdQlU-6JQYCdsFm6518UUHA8cpI")
    model = genai.GenerativeModel("gemini-pro")

    #guarda las entradas y relaciona las respuestas
    chat_historia = []

    while True:
        pregunta = input("Hazme una pregunta: ")
        if pregunta.lower() == "salir":  # Salir cierra el programa
            break

            # guarda el rol (usuario) y el contenido (pregunta)
            chat_historia.append({"role": "user", "content": pregunta})

        # response = respuesta de la ia
        response = model.generate_content(pregunta)

        # guarda el rol (asistente) y el contenido (respuesta)
        chat_historia.append({"role": "assistant", "content": response})

        # imprime la respuesta
        print(response.text)

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
    global pregunta
    pregunta = tk.Entry(ventana, font=("Verdana", 12))
    pregunta.pack(pady=10)
    pregunta.place(x=30, y=35)

    # Botón para enviar las preguntas
    btn_enviar = CTkButton(ventana, font=("sans serif", 13), border_color=c_negro, fg_color=c_azulOscuro,
                     hover_color=c_morado, corner_radius=12, border_width=2, text="Enviar Preguntas", height=40,
                     command=Preguntar)
    btn_enviar.pack()
    btn_enviar.place(relx=0.8, rely=0.5, relwidth=0.2, relheight=0.4)

    # Área de texto para las respuestas
    global response
    response = tk.Text(ventana, font=("Verdana", 12), bg="white", wrap=tk.WORD)
    response.pack(pady=50, padx=50, fill=tk.BOTH, expand=True)
    response.config(state=tk.DISABLED)

    ventana.mainloop()

ir_chat()
