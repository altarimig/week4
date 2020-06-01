class Persona:
    """Variables de una persona"""
    def __init__(self, dni, nombre, apellido, sexo):
        self.dni = dni
        self.nombre = nombre
        self.apellidos = apellido
        self.sexo = sexo

x = Persona(45678912, "Miguel Angel", "Altamirano Arias", "Masculino")

print(x.dni)