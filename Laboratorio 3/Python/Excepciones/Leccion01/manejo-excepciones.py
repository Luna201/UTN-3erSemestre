resultado= None

try:
    a = int(input("Digite el primer número: "))
    b = int(input("Digite el segundo número: "))
    resultado= a/b
except TypeError as e:  #error especifico de tipeo
    print(f"TypeError - Ocurrio un error: {type(e)}")
except ZeroDivisionError as e:    #clase hija de la clase exception, es mas especifica, error de division con 0
    print(f"ZeroDivisionError - Ocurrio un error: {e}")
except Exception as e:      #  es un metodo generico. La clase padre va al final
    print(f"Exception - Ocurrio un error: {e}")
print(f"El resutado es: {resultado}")
print("seguimos....")