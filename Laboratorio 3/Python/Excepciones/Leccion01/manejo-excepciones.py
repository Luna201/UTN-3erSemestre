from Python.Excepciones.Leccion01.NumerosIgualesException import NumerosIgualesException

resultado= None

try:
    a = int(input("Digite el primer número: "))
    b = int(input("Digite el segundo número: "))
    if a == b:
        raise NumerosIgualesException("Son números iguales")    #Excepciones personalizadas
    resultado= a/b
except TypeError as e:  #error especifico de tipeo
    print(f"TypeError - Ocurrio un error: {type(e)}")
except ZeroDivisionError as e:    #clase hija de la clase exception, es mas especifica, error de division con 0
    print(f"ZeroDivisionError - Ocurrio un error: {e}")
except Exception as e:      #  es un metodo generico. La clase padre va al final
    print(f"Exception - Ocurrio un error: {e}")
else:
    print("No se arrojo ninguna excepción")
finally:    #Siempre se va a ejecutar
    print("Ejecución de este bloque finally")

print(f"El resutado es: {resultado}")
print("seguimos....")