class ersona:
    def __init__(self, id_persona, nombre, apellido, email):
        self._id_persona = id_persona
        self._nombre = nombre
        self._apellido = apellido
        self._email = email

    def __str__(self):
        return  f'''
            Id Persona: {self._id_persona},
            Nombre: {self._nombre},
            Apellido: {self._apellido},
            Email: {self._email}'''


    #Métodos getters and setters

    @property
    def id_persona(self):
        return self.id_persona

    @id_persona.setter
    def id_persona(self, id_persona):
        self._id_persona = id_persona

    @property
    def id_nombre(self):
        return self.id_nombre

    @id_nombre.setter
    def id_nombre(self, id_nombre):
        self._id_nombre = id_nombre

    @property
    def id_apellido(self):
        return self.id_apellido

    @id_apellido.setter
    def id_apellido(self, id_apellido):
        self.id_apellido = id_apellido

    @property
    def id_email(self):
        return self.id_email

    @id_email.setter
    def id_email(self, id_email):
        self.id_email = id_email