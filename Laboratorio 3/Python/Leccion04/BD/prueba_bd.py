import psycopg2  # Esto es para conectarnos a Postgres

conexion = psycopg2.connect(
    user='postgres', password='admin', host='127.0.0.1', port='5432', database='test_bd')
try:
    with conexion:
        with conexion.cursor() as cursor:
            #cursor = conexion.cursor()
            #sentencia = 'SELECT * FROM persona'     #Selecciona T0D0
            #sentencia = 'SELECT id_persona, nombre FROM persona'    Selecciona algo en particular
            #sentencia = 'SELECT * FROM persona persona WHERE id_persona= 1'     #regresa solo un registro
            sentencia = 'SELECT * FROM persona persona WHERE id_persona = %s'       #Placeholder, se pide un parametro

            id_persona = input('Digite un número para el id_persona: ')
            cursor.execute(sentencia, (id_persona,))
            #cursor.execute(sentencia)  # De esta manera ejecutamos la sentencia
            #registros = cursor.fetchall()  # Recupera todos los registros de la sentencia en una lista
            registros = cursor.fetchone()   #Recupera solo la tupla
            print(registros)
except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()
