# Q1. Arithmetic operations using user-defined functions

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

def calculate(a, b, operation="addition"):
    if operation == "addition":
        return add(a, b)
    elif operation == "subtraction":
        return subtract(a, b)
    elif operation == "multiplication":
        return multiply(a, b)
    elif operation == "division":
        return divide(a, b)
    return "Invalid operation"

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print("Addition (positional):", add(num1, num2))
print("Subtraction (keyword):", subtract(a=num1, b=num2))
print("Multiplication:", multiply(num1, num2))
print("Division:", divide(num1, num2))
print("Default operation (addition):", calculate(num1, num2))
print("Selected operation:", calculate(num1, num2, operation="multiplication"))
