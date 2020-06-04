class Person:
    """Variables perivadas"""
    __program = "Pachaqtec"

x = Person(45678912, "Miguel", "Altamirano", "Masculino")

@property
def program(self):
    return self.__program

@program.setter
def program(self, new_program):
    self.__program = new_program

print(x.getProgram)
x.setProgram("Pachaqtec - Backend")
print(x.getProgram)