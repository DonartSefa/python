

def challenge(number1, number2, operator):
    if operator == "+":
        return number1 + number2
    elif operator == "-":
        return number1 - number2
    elif operator == "*":
        return number1 * number2
    elif operator == "/":
        return number1 / number2
    else:
        raise ValueError("Invalid operation entered.")


try:

    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the second number: "))
    operator = input("Enter an arithmetic operation (+, -, *, /): ")

    result = challenge(number1, number2, operator)

    print("Result:", result)

except ValueError as ve:
    print("ValueError:", ve)

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

except Exception as e:
    print("Unexpected error occurred:", e)

finally:
    print("Program execution completed.")