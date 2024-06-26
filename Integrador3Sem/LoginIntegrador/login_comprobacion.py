import bcrypt
from LoginIntegrador.login_conexion import obtener_contraseña

def validar_ingresos(usuario, contraseña):
    try:
        contraseña_encriptada = obtener_contraseña(usuario)
        if contraseña_encriptada:
            if bcrypt.checkpw(contraseña.encode('utf-8'), contraseña_encriptada.encode('utf-8')):
                return True, "Inicio de sesión exitoso"
            else:
                return False, "Usuario o contraseña incorrectos"
        else:
            return False, "Usuario o contraseña incorrectos"
    except Exception as e:
        return False, f'Ocurrió un error: {e}'
