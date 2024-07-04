from tkinter import messagebox
import tkinter as tk
from customtkinter import CTkButton

# Colors
c_azulClaro = "#86A9FD"
c_negro = "#010101"
c_morado = "#7f5af0"
c_verde = "#2cb67d"
c_azul = "#33DDFF"
c_azulOscuro = "#2980B9"

# Variables
step = 1
tema = 0
grupos = 0
fechas = 0
lugar = 0

def write_to_file(data):
    with open("communications.txt", "a") as file:
        file.write(data + "\n")

def ir_chatbot(ventana_anterior):
    global step, tema, grupos, fechas, lugar, cuotas

    def show_step():
        text_box.config(state=tk.NORMAL)
        text_box.delete('1.0', tk.END)

        if step == 1:
            text_box.insert(tk.END, """
                __ Bienvenido a la sección de Consultas __\n
Seleccione lo que desea consultar:\n
 (1) Grupos\n (2) Fechas\n (3) Lugar de partidos\n (4) Historial de Campeones\n (5) Comunicaciones\n""")

        elif step == 2:
            if tema == 1:
                text_box.insert(tk.END, """
            ---     Formación de grupos     ---\n
 Grupo A: Argentina - Perú - Chile - Canada\n Grupo B: México - Ecuador - Venezuela - Jamaica\n
 Grupo C: Estados Unidos - Uruguay - Panamá - Bolivia\n Grupo D: Brasil - Colombia - Costa Rica - Paraguay\n

 Presione 0 para Volver\n""")
            elif tema == 2:
                text_box.insert(tk.END, """
            ---     ¿Qué fecha quiere consultar?     ---\n
 Fecha 1: Argentina vs Canada / Peru vs Chile / México vs Jamaica / Ecuador vs Venezuela /
          EE.UU vs Bolivia / Uruguay vs Panamá / Brasil vs Costa Rica / Colombia vs Paraguay\n
 Fecha 2: Argentina vs Chile / Peru vs Canada / México vs Venezuela / Ecuador vs Jamaica /
          EE.UU vs Panamá / Uruguay vs Bolivia / Brasil vs Paraguay / Colombia vs Costa Rica\n
 Fecha 3: Argentina vs Peru / Canada vs Chile / México vs Ecuador / Jamaica vs Venezuela /
          EE.UU vs Uruguay / Bolivia vs Panamá / Brasil vs Colombia / Costa Rica vs Paraguay\n
 Cuartos de Final: 1ro grupo B vs 2do grupo A / 1ro grupo A vs 2do grupo B / 1ro grupo D vs 2do grupo C / 1ro grupo C vs 2do grupo D\n
 Semifinal: Ganador (1B vs 2A) vs Ganador (1A vs 2B) / Ganador (1D vs 2C) vs Ganador (1C vs 2D)\n
 Final: Final y 3er Puesto\n

 Presione 0 para Volver""")
            elif tema == 3:
                text_box.insert(tk.END, """
           __ Lugar a jugar: __\n
 (1) Fase de grupos\n (2) Cuartos de final\n (3) Semifinales\n (4) 3er Puesto y Final\n (0) Volver\n""")

            elif tema == 4:
                text_box.insert(tk.END, """
            Los campeones de la Copa America desde 2 de julio de 1916, fecha en que se inauguro el torneo, hasta la fecha.\n
 # Uruguay= 15\n # Argentina= 15\n # Brasil= 9\n # Chile= 2\n # Paraguay= 2
 # Peru= 2\n # Colombia = 1\n # Bolivia= 1\n

 Presione 0 para Volver""")
            elif tema == 5:
                text_box.insert(tk.END, """
            Ingrese su Nombre completo, correo y número de teléfono\n
            Ejemplo: Juan Perez, juanperez@ejemplo.com, +598 99123456\n

            Presione 0 para Volver""")

        elif step == 3:
            # Process
