import psycopg2  # Esto es para conectarnos a Postgres

conexion = psycopg2.connect(
    user='postgres', password='admin', host='127.0.0.1', port='5432', database='test_bd')
try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'UPDATE persona SET NOMBRE= %s, apellido=%s, email=%s WHERE id_persona= %s '
            valores = ('Juan Carlos', 'Roldan', 'rcarlos@gmail.com', 1)    #es una tupla
            cursor.execute(sentencia, valores)
            registros_actualizados = cursor.rowcount
            print(f'Los registros insertados son: {registros_actualizados}')

except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()
