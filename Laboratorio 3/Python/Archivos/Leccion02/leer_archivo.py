
archivo= open('prueba.txt', "r", encoding='utf8')    #r=read
print(archivo.read())

archivo= open('prueba.txt', "a", encoding='utf8')    #a=append, anexar
print(archivo.read())

archivo= open('prueba.txt', "x", encoding='utf8')    #x= crear archivo
print(archivo.read())