"""def summ():
    print(5 + 10)

summ()"""

"""def summ(number1, number2=20):
    print(number1 + number2)

summ(10, 15)
summ(10)"""

"""def summ(number1, number2=20):
    print(number1)
    print(number2)
    print(number1 + number2)

summ(number2=10, number1=15)"""

"""def summ(numbers):
    result = 0
    for number in numbers:
        result += number
    print(result)

summ([4, 5])"""

"""def summ(**numbers):
    print(numbers)
    print(numbers['number1'] + numbers['number2'])

summ(number1=10, number2=20)"""

"""class Person:
    def saludar(self):
        print("Hola, como estás? ")

person = Person()
person.saludar()"""

"""class Person:
    def __init__(self):
        print("Hola, como estás? ")

person = Person()"""

"""class Person:
    def __init__(self, name, apellido):
        self.name = name
        self.apellido = apellido
        print(f"Hola, {self.name} {self.apellido}")

person = Person("Miguel", "Altamirano")"""

class Person:
    def __del__(self):
        print("La persona se está borrando de la memoria")

person = Person()

del(person)