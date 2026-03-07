class Animal:
    def __init__(self,name):
        self.name = name

    def sound(self):
        print("Some generic animal sound")

    def descripton(self):
        print(f"This is an animal named {self.name}")

class Dog(Animal):
    def __init__(self,name,breed):
        super().__init__(name)
        self.breed = breed

    def sound(self):
        super().sound()

        print("Woof!")

    def descripton(self):
        super().descripton()
        print(f"Breed: {self.breed}")

class Cat(Animal):
    def __init__(self,name,color):
        super().__init__(name)
        self.color = color

    def sound(self):
        super().sound()

        print("Meow!")

    def descripton(self):
        super().descripton()
        print(f"color: {self.color}")

animal = Animal("Generic Animal")
print(animal.sound())
print(animal.descripton())

dog = Dog("Rex","Golden Retriever")
print(dog.sound())
print(dog.descripton())

cat = Cat("Whiskers","White")

print(cat.descripton())
print(cat.sound())
