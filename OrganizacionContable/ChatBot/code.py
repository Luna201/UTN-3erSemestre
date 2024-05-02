# PROYECTO DE CHATBOT: Organización Contable

import google.generativeai as genai

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
