class Person:
    """Variables perivadas"""
    __program = "Pachaqtec"

x = Person(45678912)

def getProgram(self):
    return self.__program

def setProgram(self, new_program):
    self.__program = new_program

print(x.getProgram())
x.setProgram("Pachaqtec - Backend")
print(x.getProgram())