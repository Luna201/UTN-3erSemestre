import psycopg2  # Esto es para conectarnos a Postgres

conexion = psycopg2.connect(
    user='postgres', password='admin', host='127.0.0.1', port='5432', database='test_bd')
try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'INSERT INTO persona (nombre, apellido, email) VALUES (%s, %s, %s)'  # Placeholder, se pide un parametro
            valores = ('Carlos', 'Lara', 'clara@gmail')     # Es una tupla
            cursor.execute(sentencia, valores)
            # conexion.commit()     Esto se utiliza para guardar los cambios en la BD, con with es automatico
            registros_insertados = cursor.rowcount
            print(f'Los registros insertados son: {registros_insertados}')

except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()
