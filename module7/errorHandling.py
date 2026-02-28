
try:
    result=10/0

except ZeroDivisionError:
    print("Tried to divide by zero!")

fruits = {
    "apple": 5,
    "orange":3,
    "banana":7
}

try:
    print(fruits['cherry'])

except KeyError:
    print("The key doesn't match in the dictionary")

text = "This is not a number"

try:
    text_to_int = int(text)

except Exception as e:
    print("An error occurred",e)

try:
    result = 10/2
except ZeroDivisionError:
    print("Divided by 0")
else:
    print("Division successful. Result= ",result)

try:
    result= 10/0
except ZeroDivisionError:
    print("We have an error,we cant divide by 0")
finally:
    print("Finally block executed")

def divide_numbers(a,b):
    try:
        result = a/b
        print("The result is: ",result)
    except ZeroDivisionError:
        print("You tried to divide by 0")
    except TypeError:
        print("Invalid type for division")
    except Exception as e:
        print("Unexpected error",e)


divide_numbers(10,2)
divide_numbers(10,0)
divide_numbers(19,'2')

