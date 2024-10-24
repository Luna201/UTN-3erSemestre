class PersonaDAO:
    """
    DAO significa: Data Access Object
    CRUD significa:
        Create -> Insertar-crear
        Read   -> Seleccionar-leer
        Update -> Actualizar
    """
    _SELECCIONAR= 'SELECT * FROM persona ORDER BY id_persona'
    _INSERTAR= 'INSERT INTO persona(nombre, apellido, email) VALUES (%s, %s, %s)'
    _ACTUALIZAR= 'UPDATE persona SET nombre= %s, apellido=%s, email=%s WHERE id_persona=%s'
    -ELIMINAR= 'DELETE FROM persona WHERE id_persona=%s'