resultado= None
a= "10"
b= 0
try:
    resultado= a/b
except Exception as e:
# O except ZeroDivisionError as e:  #clase hija de la clase exception, es mas especifica, pero es mejor usar metodos genericos
    print(f"Ocurrio un error: {e}")
print(f"El resutado es: {resultado}")
print("seguimos....")