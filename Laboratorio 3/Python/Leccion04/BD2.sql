--Consulta informacion seleccionada
--SELECT * FROM persona WHERE id_persona in (1,2)
--Ingresamos un nuevo elemento a la table
--INSERT INTO persona(nombre, apellido, email) VALUES ('Carla', 'Gomez', 'cgomez@gmail.com')
--Hacemos una consulta parta ver toda la información de la tabla
-- Hay que especificar CUAL id se va a modificar sino se modifica TODO
--UPDATE persona SET nombre= 'Ivone', email= 'iesparza@gmail.com' WHERE id_persona= 3
SELECT * FROM persona
--Eliminar SIEMPRE se debe agregar el id sino BORRA TODO
--DELETE FROM persona WHERE id_persona= 3