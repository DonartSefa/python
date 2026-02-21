# from pyexpat.errors import messages
#
# import my_math
#
# from my_math import square
#
# result = my_math.square(5)
#
# print(result)
#
# result2 = square(4)
# print(result2)

import greet
metoda1 = greet.greet_person("Donart")
print(metoda1)

from packages import module1 as m1
from packages import module2 as m2
from packages import module3 as m3
import emoji

print(m1.welcome())
print(m2.greet())
print(m3.hello())

print(emoji.emojize("Python is fun :snake:"))
