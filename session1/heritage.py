class Action(Person):
    pass

class Action(Person):
    def __init__(self, dni, nombre, apellido, sexo, accion):
        super().__init__(dni, nombre, apellido, sexo)
        self.action = Action
