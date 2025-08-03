# calculator program to make example function in python
def add(num1, num2):
    "this function to add two numbers and return the result"
    result = num1 + num2
    return result


def subtract(num1, num2):
    "this function to subsctract two numbers and return the result"
    result = num1 - num2
    return result


def multiply(num1, num2):
    "this function to multiply two numbers and return the result"
    result = num1 * num2
    return result


def divide(num1, num2):
    "this function to divide two numbers and return the result"
    if num2 == 0:
        print("Error: cannot divide by zero")
        return None  # Indicate an invalid result
    else:
        result = num1 / num2
        return result


print("Welcome to the calculator program")
num1 = int(input("Enter number one = "))
num2 = int(input("Enter number two = "))
print("1. Add\n2. Subtract\n3. Multiply\n4. Divide")


# give the user choices to be chosen
choice = int(input("Enter your choice: "))
if choice == 1:
    print(add(num1, num2))
elif choice == 2:
    print(substract(num1, num2))
elif choice == 3:
    print(multiply(num1, num2))
elif choice == 4:
    print(divide(num1, num2))
else:
    print("Invalid choice")
