# Declaramos una variable
try:
    archivo = open("prueba.txt", "w", encoding='utf8')  # La w es de write. Open puede arrojar una exception(colocar try). utf8 muestra caracteres con acentos
    archivo.write('Programamos con diferentes tipos de archivos, ahora en txt.\n')
    archivo.write('Los acentos son importantes para las palabras\n')
    archivo.write('Como por ejempo: acción, ejecución y producción\n')
    archivo.write('Las letras son:\nr read,\na append anexa,\nw write escribe,\nx crea un archivo')
    archivo.write('\nt es para texto o text,\nb para archivos binarios (image, video),\nw+ o r+ para escribir y leer\n ')
    archivo.write("Saludos a todos los alumnos de la tecnicatura")
    archivo.write('Con esto terminamos')
except Exception as e:
    print(e)
finally:  # siempre se ejecuta
    archivo.close()  # con esto se debe cerrar el archivo
#archivo.write('Todo quedo perfecto') ERROR, no se puede modificar el archivo una vez se cerró
