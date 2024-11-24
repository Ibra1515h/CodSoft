def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

while True:
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Enter the operation (+, -, *, /): ")

        if operation not in operations:
            print("Invalid operation. Please try again.")
            continue

        result = operations[operation](num1, num2)
        print(f"Result: {result}")

        another = input("Do you want to perform another calculation? (yes/no): ")
        if another.lower() != 'yes':
            break

    except ValueError:
        print("Invalid input. Please enter valid numbers.")
    except Exception as e:
        print(f"An error occurred: {e}")

print("Thank you for using the calculator!")