class Person:
    def __init__(self,name,surname,age,height):
        self.name = name
        self.surname = surname
        self.age = age
        self.height = height

    def greet(self):
        print("The name of the person is ",self.name,",the surnamme of the person is ",self.surname, ",the age of the person is ",self.age,",and the height of the person is ",self.height)

person1 = Person("Donart","Sefa","17","185cm")
person2 = Person("Diar","Berisha","18","180cm")

print(person1.greet())
print(person2.greet())