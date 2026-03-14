class Dog():
    def __init__(self,name):
        self.name = name

    def sound(self):
        print(f"{self.name} make the sound: Woof!) ")

class Cat():
    def __int__(self,name):
        self.name = name

    def sound(self):
        print(f"{self.name} makes the sound: Meow!")

class Bird():
    def __init__(self,name):
        self.name = name

    def sound(self):
        print(f"{self.name} makes the soundL: Chirp!")

dog = Dog("Buddy")

bird = Bird("Tweetie")

for animal in (dog,bird):
    animal.sound()

