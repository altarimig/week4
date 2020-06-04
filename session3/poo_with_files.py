class Person():
    def __init__(self, nombre, edad, sexo):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo

class File():
    def __init__(self, file_name):
        self.file_name = file_name

def show_file(self):
    try:
        file = open("archivo.txt", 'r')
    for line in file.readlines():
        print(line)
    except Exception as e:
        print("error: ", str(e))

    else:
        file.close()

def add_person(self, person):
    try:
        file = open(self.file_name, 'a')
        add_text = "{},{},{} \n".format(person.name, person.age, person.sex)
        file.write(add_text)
    except Exceptionas e:
        print("error : ", str(e))
    else:
        file.close()
        print(file)
person = Person("Miguel", 36, "Maxho")
file = File("thefile.txt")
file.add_person(person)
file.show_file()