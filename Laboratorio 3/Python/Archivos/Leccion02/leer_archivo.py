archivo = open('prueba.txt', "r", encoding='utf8')  # r=read; a=append, anexar; x= crear archivo
                #se coloca la direccion de archivo si hace falta
#print(archivo.read(15))
#print(archivo.read(5))      #Continuamos desde la linea anterior
#print(archivo.readline())
#print(archivo.readline())

#Vamos a iterar el archivo, cada una de las líneas
#for linea in archivo:
    # print(linea)      Iteramos todos los elementos del archivos
#print(archivo.readlines())    # Accedemos al archivo como si fuera una lista
#print(archivo.readlines()[11])  #accedemos a la linea especifica de la lista

#Anexamos información, copiamos a otro
archivo2= open("copia.txt", "a", encoding="utf8")
archivo2.write(archivo.read())
archivo.close()     #cerramos el archivo
archivo2.close()      #cerramos el 2do archivo

print("Se ah terminado el proceso de leer y copiar archivos")