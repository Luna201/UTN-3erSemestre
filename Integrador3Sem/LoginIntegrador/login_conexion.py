import psycopg2

def obtener_contraseña(usuario):
    try:
        conexion = psycopg2.connect(user='postgres',
                                    password='admin',
                                    host='127.0.0.1',
                                    port='5432',
                                    database='integrador_constructora')

        with conexion:
            with conexion.cursor() as cursor:
                query = "SELECT contrasenia FROM usuarios WHERE usuario = %s"
                cursor.execute(query, (usuario,))
                resultado = cursor.fetchone()
                if resultado:
                    return resultado[0]
                else:
                    return None
    except Exception as e:
        raise e
    finally:
        if 'conexion' in locals():
            conexion.close()
