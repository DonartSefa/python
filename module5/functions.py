# def greet():
#     print("Hello World")
#
# greet()
#
# def greet_person(name):
#     print("Hello", name)
#
# greet_person("Donart")
#
# def greet2(name):
#     global message
#     message = f"Hello, {name}"
#
#
# greet2("Donart")
# print(message)
#
# greeting = "Hello"
# name = "Donart"
# def greet():
#     global greeting
#     greeting = "Goodbye"
#
#     name = "Diar"
#
#     message = f"{greeting},{name}"
#     print(message)
#
# greet()

def greet_person(name,greeting="Hello"):
    message = f"{greeting},{name}"
    return message
metoda1 = greet_person("Donart")

metoda2 = greet_person("Diar", "Hi")

print(metoda1)
print(metoda2)